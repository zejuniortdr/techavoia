/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


// Intervalo de polling em milissegundos (por exemplo, 5000 milissegundos = 5 segundos)
const interval = 900;

// Função para parar o polling
function stopPolling() {
    clearInterval(polling);
    console.log('Polling interrompido.');
  }

// Função que faz a requisição para o endpoint
function shortPolling() {
  // Exemplo para parar o polling após 30 segundos
  setTimeout(stopPolling, 30000);

  fetch(location.pathname+"/json/")
    .then(response => {
      if (!response.ok) {
        throw new Error('Falha na requisição: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
        if(data.summary != null){
            stopPolling();
            document.getElementById("subheading").textContent = data.summary;
            document.getElementById("text_content").innerHTML = data.text;
        }
    })
    .catch(error => {
      console.error('Erro durante a requisição:', error);
    });
}


function like(){
  fetch(location.pathname+"/like/")
    .then(response => {
      if (!response.ok) {
        throw new Error('Falha na requisição: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
        if(data.likes != null){
            document.getElementById("likes").textContent = data.likes;
        }
    })
    .catch(error => {
      console.error('Erro durante a requisição:', error);
    });
}

function dislike(){
  fetch(location.pathname+"/dislike/")
    .then(response => {
      if (!response.ok) {
        throw new Error('Falha na requisição: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
        if(data.dislikes != null){
            document.getElementById("dislikes").textContent = data.dislikes;
        }
    })
    .catch(error => {
      console.error('Erro durante a requisição:', error);
    });
}
