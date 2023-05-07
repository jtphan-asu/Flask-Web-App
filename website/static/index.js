
//Function to delete note by sending POST request to backend with noteId
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {

        //reload window with get request
        window.location.href = "/"
    })
}