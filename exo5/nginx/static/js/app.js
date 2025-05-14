document.addEventListener('DOMContentLoaded', function() {
    // Éléments DOM
    const taskForm = document.getElementById('task-form');
    const tasksList = document.getElementById('tasks-list');
    const apiStatus = document.getElementById('api-status');
    
    // Vérifier l'état de l'API
    checkApiStatus();
    
    // Charger les tâches existantes
    loadTasks();
    
    // Gestionnaire de soumission du formulaire
    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        
        createTask(title, description);
    });

    // Vérifier l'état de l'API
    function checkApiStatus() {
        fetch('/api/health')
            .then(response => response.json())
            .then(data => {
                apiStatus.textContent = `Connecté - Statut: ${data.status} (${new Date(data.timestamp).toLocaleString()})`;
                apiStatus.classList.add('connected');
            })
            .catch(error => {
                apiStatus.textContent = `Erreur de connexion: ${error.message}`;
                apiStatus.classList.add('error');
            });
    }
    
    // Charger les tâches
    function loadTasks() {
        fetch('/api/tasks')
            .then(response => response.json())
            .then(data => {
                renderTasks(data.tasks);
            })
            .catch(error => {
                tasksList.innerHTML = `<p class="error">Erreur lors du chargement des tâches: ${error.message}</p>`;
            });
    }
    
    // Créer une nouvelle tâche
    function createTask(title, description) {
        fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, description }),
        })
        .then(response => response.json())
        .then(data => {
            // Réinitialiser le formulaire
            taskForm.reset();
            // Recharger les tâches
            loadTasks();
        })
        .catch(error => {
            alert(`Erreur lors de la création de la tâche: ${error.message}`);
        });
    }
    
    // Mettre à jour une tâche
    function updateTask(taskId, updates) {
        fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updates),
        })
        .then(response => response.json())
        .then(data => {
            // Recharger les tâches
            loadTasks();
        })
        .catch(error => {
            alert(`Erreur lors de la mise à jour de la tâche: ${error.message}`);
        });
    }
    
    // Afficher les tâches
    function renderTasks(tasks) {
        if (tasks.length === 0) {
            tasksList.innerHTML = '<p>Aucune tâche pour le moment.</p>';
            return;
        }
        
        tasksList.innerHTML = '';
        tasks.forEach(task => {
            const taskEl = document.createElement('div');
            taskEl.className = 'task-item';
            taskEl.innerHTML = `
                <div class="task-header">
                    <span class="task-title">${task.title}</span>
                    <span class="task-status ${task.done ? 'done' : 'pending'}">${task.done ? 'Terminée' : 'En cours'}</span>
                </div>
                <div class="task-description">${task.description || 'Pas de description'}</div>
                <div class="task-date">Créée le ${new Date(task.created_at).toLocaleString()}</div>
                <div class="task-actions">
                    <button class="toggle-status" data-id="${task.id}">${task.done ? 'Marquer comme non terminée' : 'Marquer comme terminée'}</button>
                </div>
            `;
            
            // Ajouter un gestionnaire d'événements pour le bouton de changement de statut
            taskEl.querySelector('.toggle-status').addEventListener('click', function() {
                const taskId = this.getAttribute('data-id');
                updateTask(taskId, { done: !task.done });
            });
            
            tasksList.appendChild(taskEl);
        });
    }
}); 