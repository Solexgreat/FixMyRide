import React from 'react'

function Nav() {

	return (
		<nav className='nav-bar'>
			<div className="logo">
				<h1>FixMyRide</h1>
			</div>
			{/*mobile menu*/}
			<div className="menu-bar">
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
			</div>
			<ul className={`nav-item ${menuOpen ? visible: " "}`}>
				<li><a href='#Home'>Home</a></li>
				<li><a href='#About'>About</a></li>
				<li><a href='#Service'>Services</a></li>
				<li><a href='#Contact Us'>Contact Us</a></li>
			</ul>
			<div className="registration-btn">
				<button>Sign in</button>
				<button>Sign up</button>
			</div>
		</nav>
	)
}

export default Nav