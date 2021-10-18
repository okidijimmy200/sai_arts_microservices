import React, { useState,useEffect} from 'react'
import SliderContent from './SliderContent'
import ImageSlider from './SliderComponents/ImageSlider'
import Dots from './SliderComponents/Dots';
import Arrows from './SliderComponents/Arrows';


const len = ImageSlider.length - 1;

export default function Slider(props) {
    const [activeIndex, setActiveIndex] = useState(0)

    const handleClickNext = () => {
        setActiveIndex(activeIndex === len ? 0 : activeIndex + 1)
    } 
    useEffect(() => {
        const handleAutoPlay = setInterval(handleClickNext, 5000)
        return () => clearInterval(handleAutoPlay)
    }, [handleClickNext])
    
    return (
        <div className='slider-container'>
            <SliderContent activeIndex={activeIndex} imageSlider={ImageSlider}/>
            <Arrows 
            prevSlide={() => 
                setActiveIndex(activeIndex < 1 ? len : activeIndex - 1)} 
                
            nextSlide={() => 
                    setActiveIndex(activeIndex === len ? 0 : activeIndex + 1)}    
            />
            <Dots activeIndex={activeIndex} imageSlider={ImageSlider} onClick={activeIndex => setActiveIndex(activeIndex)} />
            
        </div>
    )
}
