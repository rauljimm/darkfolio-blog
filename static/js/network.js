// Network animation using vanilla JS
document.addEventListener('DOMContentLoaded', function() {
    // Canvas setup
    const canvas = document.getElementById('network-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const container = canvas.parentElement;
    
    // Set canvas to full width/height
    function resizeCanvas() {
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
    }
    
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    // Node class
    class Node {
        constructor(x, y, radius, speed) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.color = '#2196f3';
            this.alpha = 0.7;
            this.speed = speed;
            this.directionX = Math.random() < 0.5 ? -1 : 1;
            this.directionY = Math.random() < 0.5 ? -1 : 1;
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.globalAlpha = this.alpha;
            ctx.fill();
            ctx.globalAlpha = 1;
        }
        
        update() {
            // Boundary check
            if (this.x + this.radius > canvas.width || this.x - this.radius < 0) {
                this.directionX *= -1;
            }
            if (this.y + this.radius > canvas.height || this.y - this.radius < 0) {
                this.directionY *= -1;
            }
            
            // Move node
            this.x += this.speed * this.directionX;
            this.y += this.speed * this.directionY;
            
            this.draw();
        }
    }
    
    // Edge class
    class Edge {
        constructor(startNode, endNode) {
            this.startNode = startNode;
            this.endNode = endNode;
            this.color = '#64b5f6';
            this.maxDistance = 350; // Maximum distance to draw an edge (increased from 300)
        }
        
        draw() {
            const dx = this.endNode.x - this.startNode.x;
            const dy = this.endNode.y - this.startNode.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < this.maxDistance) {
                // The further apart, the more transparent
                const alpha = 1 - distance / this.maxDistance;
                ctx.beginPath();
                ctx.moveTo(this.startNode.x, this.startNode.y);
                ctx.lineTo(this.endNode.x, this.endNode.y);
                ctx.strokeStyle = this.color;
                ctx.globalAlpha = alpha * 0.6; // Increased from 0.5 for better visibility
                ctx.lineWidth = 1;
                ctx.stroke();
                ctx.globalAlpha = 1;
            }
        }
    }
    
    // Create nodes
    const nodeCount = Math.max(25, Math.floor(canvas.width * canvas.height / 15000)); // Increased node count
    const nodes = [];
    
    for (let i = 0; i < nodeCount; i++) {
        const radius = Math.random() * 2 + 3;
        const x = Math.random() * (canvas.width - radius * 2) + radius;
        const y = Math.random() * (canvas.height - radius * 2) + radius;
        const speed = Math.random() * 0.5 + 0.2; // Slightly faster
        
        nodes.push(new Node(x, y, radius, speed));
    }
    
    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw all possible edges
        for (let i = 0; i < nodes.length; i++) {
            for (let j = i + 1; j < nodes.length; j++) {
                const edge = new Edge(nodes[i], nodes[j]);
                edge.draw();
            }
        }
        
        // Update and draw all nodes
        nodes.forEach(node => node.update());
    }
    
    animate();
    
    // Add mouse interaction
    const mouse = {
        x: null,
        y: null,
        radius: 150 // Increased from 100
    };
    
    canvas.addEventListener('mousemove', function(e) {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
        
        // Repel nodes
        nodes.forEach(node => {
            const dx = node.x - mouse.x;
            const dy = node.y - mouse.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < mouse.radius) {
                const forceX = dx / distance * 5;
                const forceY = dy / distance * 5;
                node.x += forceX;
                node.y += forceY;
            }
        });
    });
}); 