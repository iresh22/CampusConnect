        const loginScreen = document.getElementById('loginScreen');
        const appContainer = document.getElementById('appContainer');
        const loginForm = document.getElementById('loginForm');
        const logoutBtn = document.getElementById('logoutBtn');
        
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            if (email && password) {
                loginScreen.style.display = 'none';
                appContainer.style.display = 'block';
                localStorage.setItem('isLoggedIn', 'true');
            }
        });
        
        logoutBtn.addEventListener('click', function() {
            loginScreen.style.display = 'flex';
            appContainer.style.display = 'none';
            localStorage.removeItem('isLoggedIn');
        });
        
        window.addEventListener('DOMContentLoaded', function() {
            const isLoggedIn = localStorage.getItem('isLoggedIn');
            if (isLoggedIn) {
                loginScreen.style.display = 'none';
                appContainer.style.display = 'block';
            }
        });