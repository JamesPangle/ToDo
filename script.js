const wrapper2 = document.querySelector(".wrapper"),
    header2 = wrapper.querySelector("header");

    function onDrag({movementX, movementY}){
      let getStyle = window.getComputedStyle(wrapper);
      let leftVal = parseInt(getStyle.left);
      let topVal = parseInt(getStyle.top);
      wrapper2.style.left = `${leftVal + movementX}px`;
      wrapper2.style.top = `${topVal + movementY}px`;
    }

    header2.addEventListener("mousedown", ()=>{
      header2.classList.add("active");
      header2.addEventListener("mousemove", onDrag);
    });

    document.addEventListener("mouseup", ()=>{
      header2.classList.remove("active");
      header2.removeEventListener("mousemove", onDrag);
    });