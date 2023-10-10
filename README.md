# Passphrase Generator

This is a userscript that generates a passphrase for input fields using a hardcoded wordlist from EFF 2016. The generated passphrase is a combination of four randomly selected words from the wordlist, with the first letter of each word capitalized.

## Installation

To use this script, you need to have a userscript manager installed in your browser. One popular userscript manager is Tampermonkey, which is available for Chrome, Firefox, Safari, and other browsers. 

Once you have a userscript manager installed, you can install the Passphrase Generator script by following these steps:

1. Click on the Tampermonkey icon in your browser toolbar.
2. Click on "Create a new script".
3. Copy the contents of the PassphraseGenerator.js file and paste it into the editor.
4. Save the script by pressing Ctrl+S or clicking on "File" > "Save".

## Usage

To generate a passphrase, navigate to a webpage with an input field and click on the field to select it. Then, right-click anywhere on the page and select "Generate Passphrase" from the context menu: Right-click -> Tampermonkey -> Passphrase Generator -> Generate passphrase. If the selected input field has the type attribute set to password, the generated passphrase will be typed as a password. The passphrase will also be copied to the clipboard.

If the selected input field has the type attribute set to password, the generated passphrase will be typed as a password.

## Customization

If you want to customize the wordlist used by the script, you can modify the wordlist array in the PassphraseGenerator.js file. Simply replace the existing words with your own words, making sure to enclose each word in quotes and separate them with commas.

## Credits

This script uses a wordlist from the Electronic Frontier Foundation (EFF) Diceware project. The wordlist is licensed under the Creative Commons Attribution 3.0 License.