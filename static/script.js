

document.querySelectorAll("#delete").forEach(img =>{
    img.addEventListener('click', ()=>{
    alert('Contact Deleted!');
});
});

document.querySelector("#editForm").addEventListener('submit', (e)=>{
    alert("Contact Updated");
});
