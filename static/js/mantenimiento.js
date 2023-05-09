const pendingForms = new WeakMap()
function showContent(index){
    const sections  = document.querySelectorAll('.body_item')
    for(let i = 0; i < sections.length; i++){
        const section = sections[i]
        if(i === index){
            section.classList.add('body_item_active')
            if(i == 0){
               
            }
            else if(i == 1){
              
            }
            else if(i == 2){
               
            }
            else if(i == 3){

            }
            else if(i == 4){

            }
            else if(i == 5){

            }
            else if(i == 6){

            }
            else if(i == 7){

            }
            else if(i == 8){

            }
            else if(i == 9){

            }
            else if(i == 10){
                
            }
            else{
                section.classList.remove('body__item__active')
            }
        }
    }
}