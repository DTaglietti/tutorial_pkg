# tutorial_pkg  
**ROS 2 Humble – Publisher, Subscriber e Launch file**

---

## 📌 Descrizione del progetto
`tutorial_pkg` è un package ROS 2 sviluppato in Python (`ament_python`) che contiene:

- un **publisher**: pubblica messaggi di tipo `std_msgs/String` sul topic `/topic`
- un **subscriber**: ascolta sullo stesso topic e stampa i messaggi ricevuti
- un **file di launch**: avvia automaticamente publisher + subscriber nello stesso terminale

Questo progetto serve come base per apprendere:

- struttura di un package ROS2
- creazione di nodi in Python
- uso dei topic (pub/sub)
- creazione di un launch file
- gestione professionale con Git e GitHub

---

## 🏗 Requisiti

- Ubuntu **22.04**
- ROS 2 **Humble**
- Colcon:
  ```bash
  sudo apt install python3-colcon-common-extensions

