import React from 'react'
import '../Css-folder/footer.css'

function Footer() {

	return (
		<footer className='footer-sector'>
			<div className='FixMyRide'>
				<h2>FixMyRide</h2>
				<p>
					FixMyRIde is the most used car repair service in Nigeria
					popular for it’s quality service. We make sure to deliver
					supeiror and top notch service to our customer needs.
				</p>
			</div>
			<div className='footer-nav'>
				<div className="Sitemap">
					<ul>
						<h3>Sitemap</h3>
						<li><a href='#Home' >Home</a></li>
						<li><a href='#About' >About Us</a></li>
						<li><a href='#Services' >Services</a></li>
						<li><a href='#Contact' >Contact</a></li>
					</ul>
				</div>
				<div className="Support">
					<ul>
						<h3>Support</h3>
						<li><a href='#Live-Support' >Live Support</a></li>
						<li><a href='#Help' >Help</a></li>
						<li><a href='#FAQ' >FAQ</a></li>
						<li><a href='#Privacy-policy' >Privacy Policy</a></li>
					</ul>
				</div>
			</div>
		</footer>

	)
}

export default Footer