
// for(i = 0;i<howeverManyYouNeed;i++)
// {
//     document.getElementById("sims").innerHTML += "<p>szzsfsf</p>";
// }
//Javascript
// for(var i = 1; i <= 10; i++) {
//     var str = i + ') String of text',
//     span = document.createElement('span');

//     span.innerHTML = str;
    
//     var body = document.getElementsByTagName('body')[0];
     // body.appendChild(span);
// }
var j;


function hi() {
     var img = document.createElement('img');
     img.src = "lock the taskbar/hula.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/stitch_the_bounty_hunter_by_kcday-dacrnmx.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/cute.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/oof.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/stitch angry at you.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/Stitch with birds.jpg";
     document.getElementById('g').appendChild(img);
     var img = document.createElement('img');
     img.src = "lock the taskbar/Surfing.jpg";
     document.getElementById('g').appendChild(img);

}

function myFunction() {
     j = setInterval(hi, 900);
}   

myFunction()