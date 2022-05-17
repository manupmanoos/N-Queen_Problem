var k = 1;
window.addEventListener('load', function ()
{ 
    boardElement = document.getElementById('board');
    size = document.getElementById('size').value;
    boardElement.style.width = size*64;
    boardElement.style.height = size*64;
    boardElement.style.margin = 20 ;
    boardElement.style.border = "25px solid #333" ;
    algo = document.getElementById('algo_temp').value;
    boardElement.style.marginLeft  = "54%" ;
    boardElement.style.marginTop  = "-38%" ;
    
    if (algo == 1){
        document.getElementById("algos").selectedIndex = 0;
    }
    else if (algo ==2){
        document.getElementById("algos").selectedIndex = 1;
    }
    else {
        document.getElementById("algos").selectedIndex = 2;
    }

});
function range(start, end) {
    return Array(end - start + 1).fill().map((_, idx) => start + idx)
  }
function next_click()
{
    size = document.getElementById('size').value;
    positions = document.getElementById('Next Solution').value;
    container = document.getElementById('board');
    solution = document.getElementById('solution');
    positionList = JSON.parse(positions);
    if (k < positionList.length){
        pos = positionList[k];
        k+=1;
        lines = range(1,size*size)
        container.innerHTML ='';
        solution.innerHTML ='Solution '+ k;
        if (size%2 != 0){
            for (let i = 0; i < lines.length ; i++) {
                if (lines[i]%2 != 0) {
                    if (pos.includes(lines[i])){
                        container.innerHTML += '<div class="white">&#9819;</div>';                
                    }
                    else{
                        container.innerHTML += '<div class="white"></div>';
                    }
                    
                }
                else {
                    if (pos.includes(lines[i])){
                        container.innerHTML += '<div class="black">&#9819;</div>';
                    }
                    else{
                        container.innerHTML += '<div class="black"></div>';
                    }
                    
                }
            }
        }
        else {
            for (let i = 0; i < lines.length ; i++) {
                if (((lines[i]%2) + Math.floor((lines[i]-1)/size))%2 != 0) {
                    if (pos.includes(lines[i])){
                        container.innerHTML += '<div class="white">&#9819;</div>';                
                    }
                    else{
                        container.innerHTML += '<div class="white"></div>';
                    }
                    
                }
                else {
                    if (pos.includes(lines[i])){
                        container.innerHTML += '<div class="black">&#9819;</div>';
                    }
                    else{
                        container.innerHTML += '<div class="black"></div>';
                    }
                    
                }
            }
        }
        
    }
    else{
        solution.innerHTML ='No more solutions to display';
    }
    
}