const createBtn=document.getElementById("createBtn");
const modal=document.getElementsByClassName("modal");
const centerSection=document.getElementById("centerSection");
const joinCreateModal=document.getElementById("joinCreateModal");
const closeBtn=document.getElementsByClassName("closeBtn");
const centerSectionText=document.getElementById("centerSectionText");
const closeJoinCreateModal=document.getElementById("closeJoinCreateModal");
const closeJoinModal=document.getElementById("closeJoinModal");
const closeCreateModal=document.getElementById("closeCreateModal");
const centerSectionJoinButton=document.getElementById("centerSectionJoinButton");
centerSectionJoinButton.addEventListener('click',()=>{
  modal[0].style.display="block";
  centerSection.style.filter="blur(2px)";
})
createBtn.addEventListener('click',()=>{
  modal[0].style.display="block";
  centerSection.style.filter="blur(2px)";
})
closeJoinCreateModal.addEventListener('click',()=>{
  modal[0].style.display="none";
  centerSection.style.filter="blur(0px)";
})
closeJoinModal.addEventListener('click',()=>{
  modal[1].style.display="none";
  joinCreateModal.style.filter="blur(0px)";
})
closeCreateModal.addEventListener('click',()=>{
  modal[2].style.display="none";
  joinCreateModal.style.filter="blur(0px)";
})
function joinModal(){
  modal[1].style.display="block";
  joinCreateModal.style.filter="blur(2px)"
}

function CreateModal(){
  modal[2].style.display="block";
  joinCreateModal.style.filter="blur(2px)"
}

function getanswer(){
  console.log("hello")
}
