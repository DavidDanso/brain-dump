//live-search
jQuery(document).ready(function ($) {
  $(".live-search-list #col_section").each(function () {
    $(this).attr("data-search-term", $(this).text().toLowerCase());
  });

  $(".live-search-box").on("keyup", function () {
    var searchTerm = $(this).val().toLowerCase();

    $(".live-search-list #col_section").each(function () {
      if (
        $(this).filter("[data-search-term *= " + searchTerm + "]").length > 0 ||
        searchTerm.length < 1
      ) {
        $(this).show();
      } else {
        $(this).hide();
      }
    });
  });
});

// //
// const text = document.getElementById("note__details");

// let result = "";
// for (let i = 0; i < text.length; i++) {
//   result += text.charAt(i);
//   if ((i + 1) % 200 === 0) {
//     result += "<br>";
//   }
// }

// console.log(result);
