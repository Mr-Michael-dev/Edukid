// $(document).ready(function() {
//     const bannedWords = ['porn', 'pornn', 'violence', 'hate speech', 'sex', 'sexx', 'xxx', 'fight', 'war'];
//     const searchForm = $('#search-form');
//     const searchQueryInput = $('#search-query');
//     const searchButton = $('#search-button');
  
//     searchQueryInput.on('keyup', function() {
//       const query = $(this).val().trim();
//       let isValid = true;
  
//       // Check for banned words using regular expressions (case-insensitive)
//       for (const word of bannedWords) {
//         const regex = new RegExp(`\\b${word}\\b`, 'gi');
//         if (regex.test(query)) {
//             isValid = false;
//             $('#error').html('<span>Please enter an appropriate search term</span>');
//             break;
//         } else {
//             $('#error').html(''); // Clear any previous error message
//         }
//       }
  
//       // Enable/disable search button based on validity
//       searchButton.prop('disabled', !isValid);
//     });
  
//     // Submit form only if search query is valid
//     searchForm.submit(function(event) {
//       if (searchQueryInput.val().trim() === '') {
//         event.preventDefault(); // Prevent form submission if query is empty
//         alert('Please enter a search term.');
//       }
//     });
//   });
  