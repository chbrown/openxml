# openxml

Forked from [timetric/python-openxml](https://github.com/timetric/python-openxml).

openxml is a Python library to create and manipulate .docx and .pptx files.

The code draws heavily on Mike McCana's [python-docx library](https://github.com/mikemaccana/python-docx/).

openxml was written to support the [Timetric](http://timetric.com) data visualization platform.

# Word Usage

To create a .docx file, suitable for use with Microsoft Word, do the following:

    from openxml.docx import Document
    d = Document.create()
    d.add_heading('Document heading')
    d.add_para('This is some text in the document')
    d.add_picture('image1.png')
    d.save('document.docx')

See the source code in docx.py for further details.

# Powerpoint Usage

To create a .pptx file, suitable for use with Microsoft Powerpoint, do the following:

    from openxml.pptx import Document
    d = Document.create()
    s = d.add_slide()
    s.add_heading('Document heading')
    s.add_para('This is some text in the document')
    s.add_picture('image1.png')
    d.save('document.pptx')

See the source code in pptx.py for further details.

# License

Portions Copyright Mike McCana (MIT Licensed)
Copyright Timetric Ltd., 2012. (No license specified)
Copyright Christopher Brown, 2013 (MIT Licensed)
