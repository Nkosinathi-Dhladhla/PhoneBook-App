


document.querySelectorAll("#delete").forEach(img =>{

    if(img){
        img.addEventListener('click', function(e){
            const confirmed = confirm("Are you sure you want to delete this contact");
            if (!confirmed){
                e.preventDefault();
            }
        });
    }
});

document.querySelector("#editForm").addEventListener('submit', (e)=>{
    alert("Contact Updated");
});
