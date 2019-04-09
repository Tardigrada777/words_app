
function generateQustion(){
    eel.question()(setQuestion)
}

function setQuestion(question){
    let as = document.getElementById('answs')
    let result = document.getElementById('res')
    document.getElementById('question').innerHTML = ''
    as.innerHTML = ''
    res.innerHTML = ''
    
    document.getElementById('question').innerHTML = question.word

    let A = document.createElement('li')
    let B = document.createElement('li')
    let C = document.createElement('li')
    let D = document.createElement('li')

    A.innerHTML = question.a
    B.innerHTML = question.b
    C.innerHTML = question.c
    D.innerHTML = question.d

    as.appendChild(A)
    as.appendChild(B)
    as.appendChild(C)
    as.appendChild(D)

    li = Array.from(as.querySelectorAll('li'))
    li.map(l => {
        l.addEventListener('click', (e) => {
            

            if (e.target.textContent == question.right_answ){
                result.innerHTML = 'Right! Awesome!'
                result.setAttribute(
                    'style',
                    'transform: translateX(0px); opacity: 1; color: #28ff73;'
                )
            } else {
                result.innerHTML = 'Wrong...'
                result.setAttribute(
                    'style',
                    'transform: translateX(0px); opacity: 1; color: #ff3860;'
                )
            }
            // console.log(e.target.textContent)
            // console.log(question.right_answ)
        })
    })
}

