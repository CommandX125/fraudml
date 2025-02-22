document.addEventListener("DOMContentLoaded", function () {
    // Smooth scrolling when clicking on menu items
    document.querySelectorAll('.menu a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href').substring(1); 
            if (targetId !== "dashboard") { // Allow dashboard link to function normally
                e.preventDefault();
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    window.scrollTo({
                        top: targetSection.offsetTop - 50,
                        behavior: 'smooth'
                    });
                } else {
                    console.error(`Section with ID "${targetId}" not found.`);
                }
            }
        });
    });

    // Fade-in effect on scroll
    window.addEventListener("scroll", function () {
        document.querySelectorAll(".content").forEach(section => {
            const position = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;

            if (position < windowHeight - 100) {
                section.classList.add("active");
                console.log(`${section.classList[1]} is active`); // Log which section is activated
            }
        });
    });
});
