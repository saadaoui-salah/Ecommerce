const profile = document.getElementById('user-dropdown')
const menu  = document.getElementById('dropdown-menu')
const searchBtn = document.getElementById('search-btn')
const searchInpt = document.getElementById('search-inpt')

profile.addEventListener('click', (e) => {
	if (menu.className.includes('fixed')){
		menu.className = menu.className.replace('fixed', 'hidden')
	} else {
		menu.className = menu.className.replace('hidden', 'fixed')
	}
})

searchBtn.addEventListener('click',() => {
	if (searchInpt.value != ""){

		window.location.href = `${window.location.href}/q=${JSON.stringify(searchInpt.value)}`
	}	
})