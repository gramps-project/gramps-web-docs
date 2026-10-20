There are two ways to add a new media file (an image, audio file, video file, or any other file), and existing media files can be linked to new objects as they are created:

## Add a new standalone media file

To add a standalone media file, click the + icon in the top app bar and select "Media Object".

Click on "select a file" to select a file from your computer. On a mobile device, clicking this button will give you the option of directly taking a photo with your device's camera.

Optionally,

- enter a description of the media file under "title"
- enter a date
- set the media file as private (which will make it visible only to users with sufficient authorization)

Click "add" to upload the file and create the media object.

## Add a new media file and link it to another object

The following object types in Gramps can have media objects attached: people, families, events, places, sources, and citations.

In the detail view of any object, click the blue edit button in the bottom right (if you do not see it, your user does not have edit permissions). Click on the "gallery" tab and click the blue + button.

A dialog will open that offers the same fields as described in the previous section. Click "save" to upload the file, add a new media object, and link it to the viewed object.

## Profile pictures

The first image in a person's gallery is used as their profile picture. In edit mode, it is marked with a "Profile picture" badge. To use a different image, move it to the first position with the arrow buttons on the gallery thumbnails.

If a person has no media yet, edit mode shows an **Add profile picture** placeholder instead. Click it to upload a new media file or select an existing one.

## Link existing media files when creating an object

When you create a new person, family, event, place, source or citation, the form has a "Media" section. There you can select one or more existing media objects, which are linked to the new object when you save it.

When you create a person together with their birth and death events, the selected media objects are linked to the person only, not to the events.

## Text recognition (OCR)

If the server administrator has enabled OCR support, a "Text Recognition" button appears below the image in a media object's detail view.

Click "Text Recognition", choose the language of the text shown in the image, then click "Run". The image is processed with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and the recognized text is displayed below.

If your user has edit permissions, click "Save as Note" to create a new note (of type "Transcript") containing the recognized text and link it to the media object.

!!! tip
    OCR accuracy depends heavily on image quality and the selected language. If the result looks wrong, try a different language – for example, historical German documents often need the Fraktur variant rather than plain German.