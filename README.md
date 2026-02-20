# WLM — World Model Interpreter  
**World Model Output → Dimensional Structure**

The **World Model Interpreter (WMI)** is Layer 2 of the WLM structural protocol stack.  
It converts world‑model outputs (video, physics, spatial predictions) into **interpretable dimensional structure**.

WMI is not a vision model.  
WMI is a **structure interpreter**.

---

# 🌐 Purpose

Modern world models can predict:

- video frames  
- depth maps  
- segmentation  
- physics  
- trajectories  

But they cannot **explain** what they predict.

WMI solves this by converting raw world‑model outputs into:

- spatial anchors  
- temporal anchors  
- affordances  
- causal world structure  

This allows agents to **understand** the world, not just see it.

---

# 🧩 Core Components

### **1. Spatial Anchors**
Extracts:

- objects  
- positions  
- regions  
- topology  
- spatial relations  

### **2. Temporal Anchors**
Extracts:

- event boundaries  
- temporal order  
- motion vectors  
- causal transitions  

### **3. Affordances**
Extracts:

- what actions are possible  
- what actions are blocked  
- what actions are dangerous  
- what actions are optimal  

### **4. Structure Hooks**
Converts world structure → WLM dimensional structure.

---

# 📦 Installation

```
pip install wlm-world-model-interpreter
```

---

# 🧪 Example

```python
from wlm_world_model_interpreter import interpret

frame = load_video_frame("forest_wolf.png")
structure = interpret(frame)

print(structure)
```

Output (MVP):

```json
{
  "objects": ["wolf", "forest"],
  "spatial": {"wolf": [12, 44], "forest": "background"},
  "temporal": {"motion": "still"},
  "affordances": ["approach", "observe"],
  "causal": ["wolf injured → reduced mobility"]
}
```

---

# 📜 License

MIT License © 2026 Wujie Gu
