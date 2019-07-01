import pytest

SAMPLE_DOCUMENT = """\
<h1 id='fYbACALIBgJ'>Wut</h1>
<blockquote id='fYbACACVwyG'>Quote block is here</blockquote>
<h1 id='fYbACAYXzKA'>Headline Level one</h1>
<p id='fYbACA5Z3bB' class='line'>Hyperlinks:</p>
<div data-section-style='5'>
    <ul id='fYbACAubxS8'>
        <li id='fYbACAgNviX' class='' value='1'>
            <span id='fYbACAgNviX'>Email:\xa0
                <a href=\"mailto:j@jstvz.org\">j@jstvz.org</a>
            </span>
            <br/>
        </li>
        <li id='fYbACANpcGM' class=''>
            <span id='fYbACANpcGM'>URL:\xa0
                <a href=\"https://example.org/\">https://example.org/</a>
            </span>
            <br/>
        </li>
        <li id='fYbACAhuJ1d' class=''>
            <span id='fYbACAhuJ1d'>
                <a href=\"https://aur.archlinux.org/packages/lorem-ipsum-generator/\">Hyperlink</a>
            </span>
            <br/>
        </li>
        <li id='fYbACAvVrF5' class=''>
            <span id='fYbACAvVrF5'>
                <control data-remapped=\"True\" id=\"fYbACAMIybe\">
                    <a href=\"https://jstvz.quip.com/lqdYAHGeQnfF\">Sample Document</a>
                </control>
            </span>
            <br/>
        </li>
        <li id='fYbACAzziBs' class=''>
            <span id='fYbACAzziBs'>Folder mention:
                <control data-remapped=\"True\" id=\"fYbACAfY8SW\">
                    <a href=\"https://jstvz.quip.com/ReUAOAMYuR3\">🔥</a>
                </control>
            </span>
            <br/>
        </li>
    </ul>
</div>
<p id='fYbACAr9mBL' class='line'>Ordered list with formatting</p>
<div data-section-style='6'>
    <ul id='fYbACAbG2YT'>
        <li id='fYbACAs7yru' class='' value='1'>
            <span id='fYbACAs7yru'>
                <b>Bold</b>
            </span>
            <br/>
        </li>
        <li id='fYbACAhizKY' class=''>
            <span id='fYbACAhizKY'>
                <i>italic</i>
            </span>
            <br/>
        </li>
        <li id='fYbACAlrufX' class=''>
            <span id='fYbACAlrufX'>
                <u>underlined</u>
            </span>
            <br/>
        </li>
        <li id='fYbACATzpJn' class=''>
            <span id='fYbACATzpJn'>
                <del>strike</del>
            </span>
            <br/>
        </li>
        <li id='fYbACAo8RzB' class=''>
            <span id='fYbACAo8RzB'>
                <code>code</code>
            </span>
            <br/>
        </li>
        <li id='fYbACA2kx1q' class=''>
            <span id='fYbACA2kx1q'>
                <del>
                    <u>
                        <i>
                            <b>bold italic strike underlined</b>
                        </i>
                    </u>
                </del>
            </span>
            <br/>
        </li>
        <li id='fYbACAYHLwQ' class=''>
            <span id='fYbACAYHLwQ'>Highlighted Red</span>
            <br/>
        </li>
        <li id='fYbACA7FZjX' class=''>
            <span id='fYbACA7FZjX'>Highlighted Green</span>
            <br/>
        </li>
    </ul>
</div>
<h2 id='fYbACAroKGJ'>Headline Level two with spreadsheet</h2>
<p id='fYbACA5lRg3' class='line'>
    <control data-remapped=\"True\" id=\"fYbACABA2tM\">
        <a href=\"https://jstvz.quip.com/3BUbAidlb2rZ\">Sample Spreadsheet</a>
    </control>
</p>
<div data-section-style='13'>
    <table id='fYbACA5PRW7' title='Sheet1' style='width: 24em'>
        <thead>
            <tr>
                <th id='fYbACA4Vodp' class='empty' style='width: 6em'>A
                    <br/>
                </th>
                <th id='fYbACArtFsK' class='empty' style='width: 6em'>B
                    <br/>
                </th>
                <th id='fYbACAAZ5wx' class='empty' style='width: 6em'>C
                    <br/>
                </th>
                <th id='fYbACA5ttU0' class='empty' style='width: 6em'>D
                    <br/>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr id='fYbACAJkdrY'>
                <td id='s:fYbACAJkdrY_fYbACAm54dz' style=''>
                    <span id='s:fYbACAJkdrY_fYbACAm54dz'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACAJkdrY_fYbACAsrNcg' style=''>
                    <span id='s:fYbACAJkdrY_fYbACAsrNcg'>Frozen Header 1</span>
                    <br/>
                </td>
                <td id='s:fYbACAJkdrY_fYbACAoehGH' style=''>
                    <span id='s:fYbACAJkdrY_fYbACAoehGH'>Frozen Header 2</span>
                    <br/>
                </td>
                <td id='s:fYbACAJkdrY_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACAJkdrY_fYbACAVnHJ8'>Frozen Header 3</span>
                    <br/>
                </td>
            </tr>
            <tr id='fYbACAJuYNC'>
                <td id='s:fYbACAJuYNC_fYbACAm54dz' style=''>
                    <span id='s:fYbACAJuYNC_fYbACAm54dz'>Col 1</span>
                    <br/>
                </td>
                <td id='s:fYbACAJuYNC_fYbACAsrNcg' style=''>
                    <span id='s:fYbACAJuYNC_fYbACAsrNcg'>10</span>
                    <br/>
                </td>
                <td id='s:fYbACAJuYNC_fYbACAoehGH' style=''>
                    <span id='s:fYbACAJuYNC_fYbACAoehGH'>10</span>
                    <br/>
                </td>
                <td id='s:fYbACAJuYNC_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACAJuYNC_fYbACAVnHJ8'>100</span>
                    <br/>
                </td>
            </tr>
            <tr id='fYbACAfXbnR'>
                <td id='s:fYbACAfXbnR_fYbACAm54dz' style=''>
                    <span id='s:fYbACAfXbnR_fYbACAm54dz'>Col 2</span>
                    <br/>
                </td>
                <td id='s:fYbACAfXbnR_fYbACAsrNcg' style=''>
                    <span id='s:fYbACAfXbnR_fYbACAsrNcg'>1</span>
                    <br/>
                </td>
                <td id='s:fYbACAfXbnR_fYbACAoehGH' style=''>
                    <span id='s:fYbACAfXbnR_fYbACAoehGH'>11</span>
                    <br/>
                </td>
                <td id='s:fYbACAfXbnR_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACAfXbnR_fYbACAVnHJ8'>12</span>
                    <br/>
                </td>
            </tr>
            <tr id='fYbACABiU39'>
                <td id='s:fYbACABiU39_fYbACAm54dz' style=''>
                    <span id='s:fYbACABiU39_fYbACAm54dz'>Col 3</span>
                    <br/>
                </td>
                <td id='s:fYbACABiU39_fYbACAsrNcg' style=''>
                    <span id='s:fYbACABiU39_fYbACAsrNcg'>10/21/2019</span>
                    <br/>
                </td>
                <td id='s:fYbACABiU39_fYbACAoehGH' style=''>
                    <span id='s:fYbACABiU39_fYbACAoehGH'>10/21/2020</span>
                    <br/>
                </td>
                <td id='s:fYbACABiU39_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACABiU39_fYbACAVnHJ8'>-366</span>
                    <br/>
                </td>
            </tr>
            <tr id='fYbACA06A5X'>
                <td id='s:fYbACA06A5X_fYbACAm54dz' style=''>
                    <span id='s:fYbACA06A5X_fYbACAm54dz'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACA06A5X_fYbACAsrNcg' style=''>
                    <span id='s:fYbACA06A5X_fYbACAsrNcg'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACA06A5X_fYbACAoehGH' style=''>
                    <span id='s:fYbACA06A5X_fYbACAoehGH'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACA06A5X_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACA06A5X_fYbACAVnHJ8'>\u200b</span>
                    <br/>
                </td>
            </tr>
            <tr id='fYbACAlZa3S'>
                <td id='s:fYbACAlZa3S_fYbACAm54dz' style=''>
                    <span id='s:fYbACAlZa3S_fYbACAm54dz'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACAlZa3S_fYbACAsrNcg' style=''>
                    <span id='s:fYbACAlZa3S_fYbACAsrNcg'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACAlZa3S_fYbACAoehGH' style=''>
                    <span id='s:fYbACAlZa3S_fYbACAoehGH'>\u200b</span>
                    <br/>
                </td>
                <td id='s:fYbACAlZa3S_fYbACAVnHJ8' style=''>
                    <span id='s:fYbACAlZa3S_fYbACAVnHJ8'>\u200b</span>
                    <br/>
                </td>
            </tr>
        </tbody>
    </table>
</div>
<h3 id='fYbACAy1Dv7'>Headline Level Three with Code Block</h3>
<pre id='fYbACAxtHLo' class='prettyprint'>def\xa0sq(param):
    <br/>\xa0 \xa0 \"\"\"Docstring\"\"\"
    <br/>\xa0 \xa0 yield\xa0{x:x**2\xa0for\xa0x in\xa0param if\xa0x in\xa0[x,\xa02**x %\xa0x]}
</pre>
<h3 id='fYbACAaMyRd'>Checklist with mentions</h3>
<div data-section-style='7'>
    <ul id='fYbACA0UChN'>
        <li id='fYbACADwFG6' class='' value='1'>
            <span id='fYbACADwFG6'>Do a thing with mention
                <control data-remapped=\"True\" id=\"fYbACAqS9HY\">
                    <a href=\"https://quip.com/MHUAEAwZ1ec\">
                        <a href=\"https://jstvz.quip.com/MHUAEAwZ1ec\">Alsojames Estevez</a>
                    </a>
                </control>
            </span>
            <br/>
        </li>
        <li
            id='fYbACAxo3jM' class=''>
            <span id='fYbACAxo3jM'>Do a\xa0 thing with date
                <control data-remapped=\"True\" id=\"fYbACAyig8h\">21 October</control>
            </span>
            <br/>
        </li>
        <li id='fYbACAR2M43' class=''>
            <span id='fYbACAR2M43'>thing with date+mention
                <control data-remapped=\"True\" id=\"fYbACARLmft\">
                    <a href=\"https://quip.com/ffHAEAEIfch\">
                        <a href=\"https://jstvz.quip.com/ffHAEAEIfch\">
                        James Estevez
                    </a>
                    </a>
                </control>\xa0
                <control data-remapped=\"True\" id=\"fYbACA9NKYA\">
                    22 October
                    </control>
            </span>
            <br/>
        </li>
        <li
                id='fYbACANbUJn' class='checked'>
            <span id='fYbACANbUJn'>Checked item</span>
            <br/>
        </li>
        <li id='fYbACAZVMb2' class='checked'>
            <span id='fYbACAZVMb2'>Checked item with mention
                <control data-remapped=\"True\" id=\"fYbACAnKrUb\">
                    <a href=\"https://quip.com/MHUAEAwZ1ec\">
                        <a href=\"https://jstvz.quip.com/MHUAEAwZ1ec\">Alsojames Estevez</a>
                    </a>
                </control>
            </span>
            <br/>
        </li>
    </ul>
</div>
<h3 id='fYbACAfEj1o'>What's a pull quote</h3>
<div data-section-style='19' class='large poll first-party-element' alt='Poll'></div>
<p id='fYbACAm6sSF' class='line'>Resolved comment anchor</p>
"""

SAMPLE_MARKDOWN = """\
## Test Entry

- [ ] markdown checklists don't work.

- But regular bullets should
  - Including nested ones
- Ending the list.

1. Enumerated lists
2. And a second item.

### Formatting
- *Italics*
- **Bold**
- __underlined__
- ~strike~
- `code`
- `r code`

#### GFM Blocks

```python
def foo(baz):
    print('NEET')
```

```r
sq <- function(x) x*x
sq(8)
```

### Tables
| header1 | header2            |
|------- |------------------ |
| value1  | `code value2`      |
| 0val    | ****bold value**** |

"""


@pytest.fixture
def current_user():
    """Pytest fixture returning a mock logged in user. """
    return {
        "name": "Humphrey Appleby",
        "emails": ["testerino@mailinator.com"],
        "id": "kcEdRH43BMb7",
        "created_usec": 1508653644990493,
        "affinity": 0.0,
        "desktop_folder_id": "PV5eFvezsdhZ ",
        "archive_folder_id": "eE1C1rY6LxAr",
        "starred_folder_id": "PwMc9KHz46Xm",
        "private_folder_id": "9ueBkmfcSetN",
        "group_folder_ids": ["w4A1xwnupSDL", "c1KVacZMh0zx", "u6Fv7Iw8jtuc"],
        "shared_folder_ids": ["boy72Hv3yIjp", "Zv2V94OxUt68", "bLpB4IjXMiGW"],
        "disabled": False,
        "profile_picture_url": "https://quip-cdn.com/fHRxNJ34DnK1kmtw8zZkD4O",
    }


@pytest.fixture
def starred_folder():
    """Pytest fixture returning a mock Quip Folder"""
    return {
        "folder": {
            "color": "manila",
            "created_usec": 1395815761359098,
            "updated_usec": 1395818386228824,
            "id": "PwMc9KHz46Xm",
            "title": "Favorites",
        },
        "member_ids": ["KaDAEAinU0V", "HFCAEA8XZiw"],
        "children": [{"thread_id": "ULJAAAkvOHx"}, {"folder_id": "LEMAOAQNQwb"}],
    }


@pytest.fixture
def document_thread():
    return {
        "thread": {
            "author_id": "ffHAEAEIfch",
            "thread_class": "document",
            "id": "fYbAAAvxPxG",
            "created_usec": 1551415281227683,
            "updated_usec": 1551674829608942,
            "title": "Wut",
            "link": "https://jstvz.quip.com/9TQhACbC29Xd",
            "type": "document",
        },
        "user_ids": ["ffHAEAEIfch"],
        "shared_folder_ids": ["ReUAOAMYuR3"],
        "expanded_user_ids": ["ffHAEAEIfch", "MHUAEAwZ1ec"],
        "invited_user_emails": [],
        "html": SAMPLE_DOCUMENT,
    }


@pytest.fixture
def child_threads():
    return {
        "IWaAAAkJhXE": {
            "thread": {
                "author_id": "ffHAEAEIfch",
                "thread_class": "document",
                "id": "IWaAAAkJhXE",
                "created_usec": 1508653773337486,
                "updated_usec": 1551415046748863,
                "title": "NO HOODIE FOR U BRAH",
                "link": "https://jstvz.quip.com/4haaAfdFBYIa",
                "type": "document",
            },
            "user_ids": ["ffHAEAEIfch"],
            "shared_folder_ids": ["CGYAOAUoyOw"],
            "expanded_user_ids": ["ffHAEAEIfch", "MHUAEAwZ1ec"],
            "invited_user_emails": [],
            "html": """
                <h1 id='IWaACAa3m4B'>NO HOODIE FOR U BRAH</h1>
                <p id='IWaACAdJYG7' class='line'>\u200b</p>
            """,
        },
        "fYbAAAvxPxG": {
            "thread": {
                "author_id": "ffHAEAEIfch",
                "thread_class": "document",
                "id": "fYbAAAvxPxG",
                "created_usec": 1551415281227683,
                "updated_usec": 1551674829608942,
                "title": "Wut",
                "link": "https://jstvz.quip.com/9TQhACbC29Xd",
                "type": "document",
            },
            "user_ids": ["ffHAEAEIfch"],
            "shared_folder_ids": ["ReUAOAMYuR3"],
            "expanded_user_ids": ["ffHAEAEIfch", "MHUAEAwZ1ec"],
            "invited_user_emails": [],
            "html": """\
            <h1 id='fYbACALIBgJ'>Wut</h1>
                <blockquote id='fYbACACVwyG'>Quote block is here</blockquote>
                <h1 id='fYbACAYXzKA'>Headline Level one</h1>
                <p id='fYbACA5Z3bB' class='line'>Hyperlinks:</p>
            """,
        },
    }


@pytest.fixture
def thread_messages():
    return [
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADAn7ufP",
            "created_usec": 1551672980428528,
            "updated_usec": 1551672980445568,
            "text": "voted for Poll option 3 with vote and comment",
            "parts": [
                ["system", "voted for Poll option 3 with vote and comment\n"],
                ["status", "via Poll"],
            ],
            "author_name": "James Estevez",
        },
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADAZ8ed0",
            "created_usec": 1551672989423385,
            "updated_usec": 1551672989436525,
            "text": "Poll comment",
            "annotation": {
                "id": "fYbACAqZe4y",
                "highlight_section_ids": ["fYbACA0fvaD"],
            },
            "author_name": "James Estevez",
        },
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADA9agdJ",
            "created_usec": 1551673012367671,
            "updated_usec": 1551673012373721,
            "text": "This comment is resolved",
            "annotation": {
                "id": "fYbACA5AARi",
                "highlight_section_ids": ["fYbACAm6sSF"],
            },
            "author_name": "James Estevez",
        },
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADAhU0fa",
            "created_usec": 1551673036106465,
            "updated_usec": 1551673043881696,
            "text": "This is a sidebar message with emoji for slightly smiling face \ud83d\ude42",
            "author_name": "James Estevez",
        },
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADAdgn2j",
            "created_usec": 1554086614441403,
            "updated_usec": 1554086614447871,
            "text": "Here is a more recent message",
            "author_name": "James Estevez",
        },
        {
            "author_id": "ffHAEAEIfch",
            "visible": True,
            "id": "fYbADABr1H6",
            "created_usec": 1560129125597670,
            "updated_usec": 1560129125611968,
            "text": "Even more recent",
            "author_name": "James Estevez",
        },
    ]


@pytest.fixture
def markdown_content():
    return SAMPLE_MARKDOWN
