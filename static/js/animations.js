document.addEventListener('DOMContentLoaded', function() {
    /**
     * Implement smooth scroll for anchor links
     */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    /**
     * Animate elements when they come into view
     */
    const animateOnScroll = () => {
        const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
        
        elementsToAnimate.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight * 0.9) {
                element.classList.add('animated');
            }
        });
    };
    
    // Initial check for elements in view
    animateOnScroll();
    
    // Check on scroll
    window.addEventListener('scroll', animateOnScroll);
    
    /**
     * Add hover effects to cards
     */
    document.querySelectorAll('.card-dark').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('card-hover');
        });
        
        card.addEventListener('mouseleave', function() {
            this.classList.remove('card-hover');
        });
    });
    
    /**
     * Typewriter effect for homepage headline 
     */
    const headlineElement = document.querySelector('.text-gradient');
    if (headlineElement && headlineElement.textContent.includes("Developer")) {
        const originalText = headlineElement.textContent;
        const developerTypes = [
            "Developer",
            "Web Developer",
            "Python Developer",
            "Django Developer",
            "Full-Stack Developer"
        ];
        
        let currentTypeIndex = 0;
        
        const updateDeveloperText = () => {
            const baseText = originalText.replace("Developer", "");
            headlineElement.textContent = baseText + developerTypes[currentTypeIndex];
            
            currentTypeIndex = (currentTypeIndex + 1) % developerTypes.length;
            
            setTimeout(updateDeveloperText, 2000);
        };
        
        setTimeout(updateDeveloperText, 2000);
    }
}); 