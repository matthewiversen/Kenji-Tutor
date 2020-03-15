function bloopes(){
    alert("BOOP INCOMING")
    imgObj = document.getElementById('chng');
    imgObj.style.display = 'block';
    var pos = 1500;
    var id = setInterval(frame, 1);
    function frame() {
        if (pos <= 500) {
            clearInterval(id);
            setTimeout(hi, 100);
        } else {
            pos = pos - 3;
            imgObj.style.left = pos + 'px'
        }
    }
    function hi() {
        imgObj.style.display = "none"
    }
}

function bloopess(){
    alert("BOOP INCOMING")
    imgObj = document.getElementById('gwasez');
    imgObj.style.display = 'block';
    var pos = -100;
    var id = setInterval(frame, 1);
    function frame() {
        if (pos >= 380) {
            clearInterval(id);
            setTimeout(hi, 1500);
        } else {
            pos = pos + 1;
            imgObj.style.top = pos + 'px'
        }
    }

    function hi() {
        imgObj.style.display = "none"
    }


    // imgObj.style.visibility='hidden';
    // imgObj.style.left = parseInt(style.left) - '100';
}





// function moveLeft(){
//     // left = parseInt(imgObj.style.left, 10);

//     for (i = 0; i < 10; i++) {
//         imgObj.style.left = (left - 5) + 'px';
//         // imgObj.style.visibility='visible';

//          animate = setTimeout(function(){moveLeft();},20); // call moveLeft in 20msec

//          //stopanimate = setTimeout(moveLeft,20);
//     // } else {
//     //     stop();
//     // }
//      //f();
// }

