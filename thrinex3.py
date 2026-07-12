import os

# Create project structure
os.makedirs("todo_app", exist_ok=True)

# ---------------- HTML ----------------
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h1>To-Do List</h1>

    <div class="input-area">
        <input type="text" id="taskInput" placeholder="Enter a task">
        <button id="addBtn">Add</button>
    </div>

    <div class="filters">
        <button data-filter="all">All</button>
        <button data-filter="active">Active</button>
        <button data-filter="completed">Completed</button>
    </div>

    <ul id="taskList"></ul>
</div>

<script src="script.js"></script>

</body>
</html>
"""

# ---------------- CSS ----------------
css = """
body{
    font-family:Arial;
    background:#f4f4f4;
    display:flex;
    justify-content:center;
    margin-top:50px;
}

.container{
    width:500px;
    background:white;
    padding:20px;
    border-radius:10px;
}

input{
    width:70%;
    padding:10px;
}

button{
    padding:10px;
    cursor:pointer;
}

li{
    display:flex;
    justify-content:space-between;
    padding:10px;
    margin:10px 0;
    background:#eee;
}

.completed{
    text-decoration:line-through;
    color:gray;
}
"""

# ---------------- JavaScript ----------------
js = """
let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const addBtn = document.getElementById("addBtn");

let filter = "all";

function save(){
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function render(){

    taskList.innerHTML="";

    tasks.forEach((task,index)=>{

        if(filter==="active" && task.completed) return;
        if(filter==="completed" && !task.completed) return;

        const li=document.createElement("li");

        li.innerHTML=`
        <span class="${task.completed?'completed':''}">
            ${task.text}
        </span>

        <div>
            <button class="toggle" data-index="${index}">
            ✓
            </button>

            <button class="edit" data-index="${index}">
            Edit
            </button>

            <button class="delete" data-index="${index}">
            Delete
            </button>
        </div>
        `;

        taskList.appendChild(li);

    });

}

addBtn.onclick=()=>{

    if(taskInput.value.trim()==="") return;

    tasks.push({
        text:taskInput.value,
        completed:false
    });

    taskInput.value="";

    save();

    render();

};

taskList.addEventListener("click",e=>{

    const index=e.target.dataset.index;

    if(e.target.classList.contains("delete")){

        tasks.splice(index,1);

    }

    if(e.target.classList.contains("toggle")){

        tasks[index].completed=!tasks[index].completed;

    }

    if(e.target.classList.contains("edit")){

        const text=prompt("Edit Task",tasks[index].text);

        if(text){
            tasks[index].text=text;
        }

    }

    save();

    render();

});

document.querySelectorAll(".filters button").forEach(btn=>{

    btn.onclick=()=>{

        filter=btn.dataset.filter;

        render();

    };

});

render();
"""

with open("todo_app/index.html","w",encoding="utf-8") as f:
    f.write(html)

with open("todo_app/style.css","w",encoding="utf-8") as f:
    f.write(css)

with open("todo_app/script.js","w",encoding="utf-8") as f:
    f.write(js)

print("To-Do App generated successfully!")
print("Files created:")
print(" - todo_app/index.html")
print(" - todo_app/style.css")
print(" - todo_app/script.js")
