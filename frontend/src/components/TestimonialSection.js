import React from 'react'
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/swiper-bundle.css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

const reviews= [
	{
		id: 1,
		Name: "John D",
		review: "I've been bringing my car here for over a year, and the service has been fantastic every single time. The mechanics are knowledgeable, honest, and always go the extra mile to explain what’s going on with my car. My vehicle has never run smoother! Highly recommend them to anyone looking for reliable and affordable repairs"
	},
	{
		id: 2,
		Name: "Sarah K",
		review: "Absolutely love this workshop! They were able to fit me in on short notice, and the entire process was smooth and stress-free. The staff is friendly, and they don’t try to upsell unnecessary services. I left feeling confident that my car was in great hands. Definitely my go-to mechanic from now on!"
	},
	{
		id: 3,
		Name: "Michael T",
		review: "Finally found a workshop that genuinely cares about their customers. They fixed my car’s brake issue quickly and even checked other parts without charging extra. The transparent pricing and honest recommendations are rare to find these days. I’ll be recommending this place to all my friends!"
	},
]

function TestimonialSection() {
	return (
			<section className="testimonial-section">
					<div className="carousel-header">
							<span className="arrow left-arrow">
    						<i className="fas fa-chevron-left"></i>
							</span>
							<h2>Testimonials</h2>
							<span className="arrow right-arrow">
									<i className="fas fa-chevron-right"></i>
							</span>
					</div>
					<Swiper
							// navigation={true}
							modules={[Navigation, Autoplay]}
							spaceBetween={30}
							slidesPerView={2}
							navigation={{
									nextEl: '.right-arrow',
									prevEl: '.left-arrow'
							}}
							loop={true}
							autoplay={{
									delay: 2500,
									disableOnInteraction: false,
							}}
					>
							{reviews.map((review) => (
									<SwiperSlide key={review.id} className="testimonial-slide">
											<div className="review-box">
													<p>{review.review}</p>
													<span>- {review.Name}</span>
											</div>
									</SwiperSlide>
							))}
					</Swiper>
			</section>
	);
}

export default TestimonialSection