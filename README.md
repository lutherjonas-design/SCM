# Attendance Tracking (Sportclub)
### **Context & Status: Paused (Architectural Case Study on System Complexity)**  
This project was designed as a learning environment to explore Django's ORM capabilities and relational database design. It was paused after reaching a structural overhead and disappearing need.

### Tech Stack
* **Framework:** Python, Django
* **Infrastructure:** Docker-ready core, localized setup scripts (`start.ps1`)
* **Configuration:** Strict environment separation via `.env` guidelines

## Key Architectural Insights & Takeaways

* **The Trap of Over-Engineering:** The initial data modeling led to a database schema with ~20 tables and a lot of containers. This complexity showed feature creep and that the architecture had become too ambiguous and heavy for a first learning project and missing pattern knowledge.
* **Shift to Component Quality:** Rather than writing repetitive code for an over-complicated system, this project forced me to pivot. I shifted my focus entirely toward smaller Projects, that offered me a more targeted learning environment.
* **Pragmatic Decision Making:** As the sports club simultaneously deployed their own external system, I chose to pause development. This allowed me to transport the lessons learned directly into my newer, more lightweight architectures.
