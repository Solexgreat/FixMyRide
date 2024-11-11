import React from 'react';
import { Icon } from '@iconify/react';

// Data for Why Choose Us section
const why_chose_us = [
	{
		id: 1,
		icon: 'mdi:check-circle', // Circle with check
		title: 'Quality and Reliability',
		description: 'Our team is committed to delivering top-notch service with a focus on quality and precision. We prioritize reliability, ensuring that each project meets high standards and is completed on time.',
	},
	{
		id: 2,
		icon: 'heroicons:wrench-screwdriver', // Wrench screwdriver
		title: 'Expertise and Innovation',
		description: 'With a skilled team dedicated to continuous learning and innovation, we stay ahead of industry trends and apply cutting-edge techniques to provide effective solutions tailored to your needs.',
	},
	{
		id: 3,
		icon: 'emojione-monotone:handshake', // Handshake
		title: 'Customer-Centric Approach',
		description: 'Your satisfaction is our priority. We focus on understanding your unique requirements and deliver customized solutions, providing transparent communication and support throughout every stage of the project.',
	},
];

function WhyChooseUs() {
	return (
		<section className="why-choose-us">
			<h2>Why Choose Us</h2>
			<div className="cards-container">
				{why_chose_us.map((item) => (
					<div key={item.id} className="card">
						<Icon icon={item.icon} className="icon" />
						<h3>{item.title}</h3>
						<p>{item.description}</p>
					</div>
				))}
			</div>
		</section>
	);
}

export default WhyChooseUs;