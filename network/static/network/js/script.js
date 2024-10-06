document.addEventListener('DOMContentLoaded', () => {

    //Function to Like post
    const like_submit = document.querySelectorAll('#like_submit');
    like_submit.forEach(like => {
        const post_id = like.getAttribute('data-post-id')
        const form_data = new FormData(like)
        const like_icon = document.querySelector(`#like_icon${post_id}`)

        let like_btn = document.querySelector(`#like_btn${post_id}`)
        like_btn.addEventListener('click', (event) => {
            event.preventDefault();
            fetch(`/like/${post_id}`, {
                method: "POST",
                body: form_data,
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector(`#like_qtd${post_id}`).innerHTML = data.likes;
                if (data.success) {
                    like_icon.classList.remove('fa-regular');
                    like_icon.classList.add('fa-solid');
                } else {
                    like_icon.classList.add('fa-regular');
                    like_icon.classList.remove('fa-solid');
                }
            })
        })
    })

    /* Function to edit post */
    const allForms = document.querySelectorAll('#edit_form');
    allForms.forEach(form => {
        form.onsubmit = (event) => {
            const post_id = form.getAttribute('data-post-id');
            const form_data = new FormData(form);
            console.log(form);
            event.preventDefault();
            
            console.log(post_id);
            fetch(`/edit/${post_id}`, {
                method: "POST",
                body: form_data,
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.new_content);
                if (data.success) {
                    console.log(data, data.new_content)
                    document.querySelector(`#content_post${post_id}`).innerHTML = data.new_content + '...'
                    document.querySelector(`#edit_form_${post_id}`).classList.add('hidden')
                } 
            })
        };
    })

    post_edit_box();
});

function post_edit_box() {

    const edit_buttons = document.querySelectorAll('.edit-post')
    edit_buttons.forEach(button => {
        button.addEventListener('click', () => {
            const postID = button.getAttribute("data-post-id");
            const edit_form = document.querySelector(`#edit_form_${postID}`);
            const form_display = window.getComputedStyle(edit_form).display;
        
            if (form_display === 'none' || form_display === '') {
                edit_form.classList.remove('hidden');
            } else {
                edit_form.classList.add('hidden');
            }
        });
    })


}