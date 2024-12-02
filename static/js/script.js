$(document).ready(function () {
    // On button click, fetch data from FastAPI
    $('#fetchData').click(function () {
        const userEmail = $('#linkInput').val(); // Capture email input
        console.log(userEmail);
        if (userEmail.trim() === '') {
            alert("Please enter a valid Link.")
            return;
        }
        $('#loadingSpinner').show();
        $('#resultTextArea').hide();

        $.ajax({
            url: "http://localhost:5000/generate", // Replace with your FastAPI endpoint
            method: "POST",
            data: JSON.stringify({ Link: userEmail }),
            contentType: "application/json",
            success: function (response) {
                console.log(response.message);
                const textarea=$('#resultTextArea')
                $('#loadingSpinner').hide();
                textarea.val(response.message).show();
                adjustTextAreaHeight(textarea);
                // $('#modalResponseBody').val(response.message);
                // $('modalResponseBody').css('visibility', 'visible');
                // alert(response.message)



            },
            error: function (error) {
                alert(error.responseText)
            }
        });
    });
});
  // Function to auto-adjust the height of the text area
  function adjustTextAreaHeight(textarea) {
    textarea.css('height', 'auto'); // Reset the height
    textarea.css('height', textarea[0].scrollHeight + 'px'); // Set the height based on scrollHeight
}