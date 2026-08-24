// ============================================
// DEVPRO — ОСНОВНЫЕ СКРИПТЫ
// ============================================

document.addEventListener('DOMContentLoaded', function() {

    // ===== АВТОМАТИЧЕСКОЕ ЗАКРЫТИЕ АЛЕРТОВ =====
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade');
            setTimeout(function() {
                alert.remove();
            }, 500);
        }, 5000);
    });

    // ===== АНИМАЦИЯ ПОЯВЛЕНИЯ КАРТОЧЕК =====
    const cards = document.querySelectorAll('.card-space');
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry, index) {
            if (entry.isIntersecting) {
                setTimeout(function() {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);
            }
        });
    }, {
        threshold: 0.1
    });

    cards.forEach(function(card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(card);
    });

    // ===== ПОДСВЕТКА АКТИВНОГО МЕНЮ =====
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function(link) {
        const href = link.getAttribute('href');
        if (href && currentPath === href) {
            link.classList.add('active');
        }
    });

});