==============================================================================
USURP (Unwanted SoUnd RePlacement)
==============================================================================
The `Child Mind Institute <http://childmind.org>`_ is developing **USURP (Unwanted SoUnd RePlacement)** as an open source software package to automate the replacement of unwanted sounds with sounds comparable to ambient noise in the rest of a given soundfile.

:Release: |release|
:Date: |today|

Links:

.. toctree::
    :maxdepth: 1

    license

- `GitHub <https://github.com/ChildMindInstitute/USURP>`_

* :ref:`modindex`
* :ref:`genindex`
* :ref:`search`

.. todo:: `sound resynthesis <https://github.com/ChildMindInstitute/USURP/sound_resynthesis>`_

..
    1. Inputs
    2. Processing
    3. Outputs
------------------------------------------------------------------------------
_`Inputs`
------------------------------------------------------------------------------
  - audio file : ``.wav`` (16-bit)
  - labels : ``.aud`` or ``.xml``

**audio file**

USURP takes 16-bit waveform soundfiles (``.wav``) as inputs. USURP is capable of converting the following filetypes to 16-bit waveforms:

  - Material eXchange Format (``.MXF`` or ``.mxf``)
  - MPEG Audio Layer III (``.mp3``)
  - 32-bit waveform (``.wav``)

**labels**
  
Currently, USURP also needs start times and stop times marked in a `labeled XML file <http://manual.audacityteam.org/man/label_tracks.html>`_, which can be generated in `Audacity <http://www.audacityteam.org/>`_. Unwanted sounds must be silenced and have their temporal boundaries marked for optimal performance.

------------------------------------------------------------------------------
_`Processing`
------------------------------------------------------------------------------
  - If necessary, convert inputs to 16-bit waveforms.
  - Clone
  
    - Find a likely ambient clip elsewhere in the file by choosing a segment with no peaks at or above a given threshold (default threshold: median of the amplitude envelope of the entire file). Copy that clip into each of the segments labeled for replacement.
    
  - Timeshift
  
    - Collapse the marked silences, shortening the file.
    
  - Output the new files.

------------------------------------------------------------------------------
_`Outputs`
------------------------------------------------------------------------------
  - Clone replacement (``.wav``)
  - Timeshifted replacement (``.wav``)
