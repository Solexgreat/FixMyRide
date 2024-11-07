import React, {useState} from 'react'

function Nav() {
	const[menuOpen, setMenuOpen] = useState(false);

	const toggleMenu = () => {
		setMenuOpen(!menuOpen);
	}
	return (
		<nav className={'nav-bar'}>
			<a href='/' className="logo">
				<h1>FixMyRide</h1>
			</a>
			{/*mobile menu*/}
			<div className="menu-bar" onClick={toggleMenu}>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
				<div className="menu-bar bar"></div>
			</div>

			<ul className="nav-item">
				<li><a href='#Home'>Home</a></li>
				<li><a href='#About'>About</a></li>
				<li><a href='#Service'>Services</a></li>
				<li><a href='#Contact Us'>Contact Us</a></li>
			</ul>

			<ul className={`nav-links ${menuOpen ? "visible": " "}`}>
				<li><a href='#Home'>Home</a></li>
				<li><a href='#About'>About</a></li>
				<li><a href='#Service'>Services</a></li>
				<li><a href='#Contact Us'>Contact</a></li>
				<li><a href='#Sing in'>Sing in</a></li>
				<li><a href='#Sing us'>Sing us</a></li>
			</ul>

			<div className="registration-btn">
				<button>Sign in</button>
				<button>Sign up</button>
			</div>
		</nav>
	)
}

export default Nav