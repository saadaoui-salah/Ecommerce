const profile = document.getElementById('user-dropdown')
const menu  = document.getElementById('dropdown-menu')
profile.addEventListener('click', (e) => {
	if (menu.className.includes('fixed')){
		menu.className = menu.className.replace('fixed', 'hidden')
	} else {
		menu.className = menu.className.replace('hidden', 'fixed')
	}
})