# Attendance Tracking (Sportclub)

⚠️ **Project Status: Paused (Architectural Case Study on System Complexity)**  
This project was explicitly designed as a learning environment to explore Django's ORM capabilities and relational database design. It was intentionally paused after reaching a structural tipping point.

## Key Architectural Insights & Takeaways

* **The Trap of Over-Engineering:** The initial data modeling led to a database schema with ~20 tables. This complexity sparked a crucial realization: the architecture had become too ambiguous and heavy for the intended scope.
* **Shift to Component Quality:** Rather than writing repetitive code for an over-complicated system, this project forced me to pivot. I shifted my focus entirely toward analyzing and fixing the interaction of components and managing technical debt.
* **Pragmatic Decision Making:** As the sports club simultaneously deployed their own external system, I chose to pause development here. This allowed me to transport the lessons learned regarding DB normalization and component decoupling directly into my newer, more lightweight architectures (like my current FastAPI and Raspberry Pi projects).

---

## 🛠️ Tech Stack & Scaffolding
* **Framework:** Django (Python)
* **Infrastructure:** Docker-ready core, localized setup scripts (`start.ps1`)
* **Configuration:** Strict environment separation via `.env` guidelines
