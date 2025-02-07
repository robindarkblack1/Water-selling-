$(document).ready(function() {
    $("#testimonial-slider").owlCarousel({
      items: 2,
      itemsDesktop: [1000, 2],
      itemsDesktopSmall: [990, 2],
      itemsTablet: [768, 1],
      pagination: true,
      navigation: false,
      // navigationText: ["", ""],
      slideSpeed: 500,
      autoPlay: true
    });
  });