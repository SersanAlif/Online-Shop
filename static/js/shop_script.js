// Flash message auto-dismiss
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(message => {
        const closeBtn = message.querySelector('.flash-close');
        
        // Auto dismiss after 5 seconds
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => message.remove(), 300);
        }, 5000);
        
        // Manual close
        closeBtn?.addEventListener('click', () => {
            message.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => message.remove(), 300);
        });
    });
});

// Add slideOutRight animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar scroll effect
let lastScrollTop = 0;
const header = document.querySelector('.header');
const scrollThreshold = 100;

window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > scrollThreshold) {
        header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.12)';
        
        if (scrollTop > lastScrollTop) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }
    } else {
        header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.08)';
        header.style.transform = 'translateY(0)';
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
}, false);

// Add transition to header
header.style.transition = 'all 0.3s ease-in-out';

// Product card animations on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.product-card, .category-card').forEach(card => {
    card.style.opacity = '0';
    observer.observe(card);
});

// Add fadeInUp animation
const animStyle = document.createElement('style');
animStyle.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(animStyle);

// Quantity input handlers
document.querySelectorAll('.quantity-input').forEach(input => {
    const minusBtn = input.querySelector('.quantity-minus');
    const plusBtn = input.querySelector('.quantity-plus');
    const valueInput = input.querySelector('.quantity-value');
    
    if (minusBtn && plusBtn && valueInput) {
        minusBtn.addEventListener('click', () => {
            let value = parseInt(valueInput.value) || 1;
            if (value > 1) {
                valueInput.value = value - 1;
            }
        });
        
        plusBtn.addEventListener('click', () => {
            let value = parseInt(valueInput.value) || 1;
            const max = parseInt(valueInput.getAttribute('max')) || 999;
            if (value < max) {
                valueInput.value = value + 1;
            }
        });
        
        valueInput.addEventListener('change', () => {
            let value = parseInt(valueInput.value) || 1;
            const min = 1;
            const max = parseInt(valueInput.getAttribute('max')) || 999;
            
            if (value < min) valueInput.value = min;
            if (value > max) valueInput.value = max;
        });
    }
});

// Loading indicator for forms
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn && !submitBtn.classList.contains('loading')) {
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;
            
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
            
            // Restore after 3 seconds if not redirected
            setTimeout(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.classList.remove('loading');
                submitBtn.disabled = false;
            }, 3000);
        }
    });
});

// Image lazy loading fallback
document.querySelectorAll('img[data-src]').forEach(img => {
    img.src = img.getAttribute('data-src');
    img.removeAttribute('data-src');
});

// Add to cart animation
document.querySelectorAll('form[action*="add_to_cart"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        const btn = this.querySelector('button[type="submit"]');
        if (btn) {
            // Create flying cart animation
            const rect = btn.getBoundingClientRect();
            const cartBtn = document.querySelector('.cart-btn');
            
            if (cartBtn) {
                const cartRect = cartBtn.getBoundingClientRect();
                
                const flyingItem = document.createElement('div');
                flyingItem.innerHTML = '<i class="fas fa-shopping-cart"></i>';
                flyingItem.style.cssText = `
                    position: fixed;
                    left: ${rect.left}px;
                    top: ${rect.top}px;
                    z-index: 9999;
                    font-size: 24px;
                    color: var(--primary);
                    pointer-events: none;
                    transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
                `;
                
                document.body.appendChild(flyingItem);
                
                setTimeout(() => {
                    flyingItem.style.left = cartRect.left + 'px';
                    flyingItem.style.top = cartRect.top + 'px';
                    flyingItem.style.opacity = '0';
                    flyingItem.style.transform = 'scale(0.3)';
                }, 10);
                
                setTimeout(() => {
                    flyingItem.remove();
                    
                    // Animate cart button
                    cartBtn.style.animation = 'cartBounce 0.5s ease';
                    setTimeout(() => {
                        cartBtn.style.animation = '';
                    }, 500);
                }, 800);
            }
        }
    });
});

// Add cart bounce animation
const cartBounceStyle = document.createElement('style');
cartBounceStyle.textContent = `
    @keyframes cartBounce {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
`;
document.head.appendChild(cartBounceStyle);

// Search auto-suggest (simple version)
const searchInput = document.querySelector('.search-input');
if (searchInput) {
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.toLowerCase();
        
        if (query.length >= 2) {
            searchTimeout = setTimeout(() => {
                console.log('Searching for:', query);
                // Add auto-suggest logic here
            }, 300);
        }
    });
}

// Price formatter
function formatPrice(price) {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0
    }).format(price);
}

// Update all prices if needed
document.querySelectorAll('[data-price]').forEach(element => {
    const price = parseFloat(element.getAttribute('data-price'));
    element.textContent = formatPrice(price);
});

// Countdown timer for deals (if needed)
function startCountdown(element, endTime) {
    const timer = setInterval(() => {
        const now = new Date().getTime();
        const distance = endTime - now;
        
        if (distance < 0) {
            clearInterval(timer);
            element.innerHTML = 'EXPIRED';
            return;
        }
        
        const hours = Math.floor(distance / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        element.innerHTML = `${hours}h ${minutes}m ${seconds}s`;
    }, 1000);
}

// Initialize countdowns
document.querySelectorAll('[data-countdown]').forEach(element => {
    const endTime = new Date(element.getAttribute('data-countdown')).getTime();
    startCountdown(element, endTime);
});

// Mobile menu toggle (if added)
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navMenu = document.querySelector('.nav-menu');

if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileMenuBtn.querySelector('i').classList.toggle('fa-bars');
        mobileMenuBtn.querySelector('i').classList.toggle('fa-times');
    });
}

// Wishlist functionality (placeholder)
document.querySelectorAll('.wishlist-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        this.classList.toggle('active');
        
        const icon = this.querySelector('i');
        if (this.classList.contains('active')) {
            icon.classList.remove('far');
            icon.classList.add('fas');
            showNotification('Added to wishlist!', 'success');
        } else {
            icon.classList.remove('fas');
            icon.classList.add('far');
            showNotification('Removed from wishlist', 'info');
        }
    });
});

// Show notification helper
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `flash-message flash-${type}`;
    notification.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'}"></i>
        <span>${message}</span>
        <button class="flash-close">&times;</button>
    `;
    
    let container = document.querySelector('.flash-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'flash-container';
        document.body.appendChild(container);
    }
    
    container.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
    
    notification.querySelector('.flash-close').addEventListener('click', () => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    });
}

// Initialize
console.log('🛒 ModernShop initialized successfully!');

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', () => {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log(`⚡ Page loaded in ${pageLoadTime}ms`);
    });
}