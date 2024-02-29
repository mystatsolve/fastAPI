function addTask() {
    // 입력 필드와 리스트 가져오기
    var taskInput = document.getElementById("taskInput");
    var taskList = document.getElementById("taskList");

    // 새로운 리스트 아이템 생성
    var newTask = document.createElement("li");
    newTask.textContent = taskInput.value;

    // 리스트에 아이템 추가
    taskList.appendChild(newTask);

    // 입력 필드 초기화
    taskInput.value = "";

    // 리스트 아이템에 클릭 이벤트 추가 (완료 토글)
    newTask.addEventListener("click", function () {
        newTask.classList.toggle("completed");
    });
}