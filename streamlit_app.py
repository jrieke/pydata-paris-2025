import time

import pandas as pd
import plotly.express as px
import pydeck as pdk
import streamlit as st

from data import df

st.logo("https://streamlit.io/images/brand/streamlit-mark-color.svg", link="https://streamlit.io")

"""
# 🇫🇷 PyData Paris 2025

Welcome! 👋 This is the Streamlit app for the talk "Beyond Prototyping: Building 
Production-Level Apps with Streamlit" by [Johannes Rieke](https://www.linkedin.com/in/johannesrieke/) and [Arnaud Miribel](https://www.linkedin.com/in/arnaudmiribel/) at 
PyData Paris 2025. 

## Advanced theming :orange-badge[🎨 Design]

Just define your theme in `.streamlit/config.toml`. This app uses:

```toml
[theme]
primaryColor = "#cb785c"
backgroundColor = "#fdfdf8"
secondaryBackgroundColor = "#ecebe3"
textColor = "#3d3a2a"
borderColor = "#d3d2ca"
showWidgetBorder = true
baseRadius = "0.75rem"
buttonRadius = "full"
font = "Space Grotesk:https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap"
headingFontWeights = [600, 500, 500, 500, 500, 500]
headingFontSizes = ["3rem", "2rem"]
codeFont = "Space Mono:https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap"
codeFontSize = ".75rem"
codeBackgroundColor = "#ecebe4"
showSidebarBorder = true
chartCategoricalColors = ["#0ea5e9", "#059669", "#fbbf24"]

[theme.sidebar]
backgroundColor = "#f0f0ec"
secondaryBackgroundColor = "#ecebe3"
headingFontSizes = ["1.6rem", "1.4rem", "1.2rem"]
dataframeHeaderBackgroundColor = "#e4e4e0"
```

Highlights:
- 47 [theming options](https://docs.streamlit.io/develop/concepts/configuration/theming)
- Google Fonts integration
- Separately configure sidebar
- (Coming soon) Custom light & dark theme

Examples ([repo](https://github.com/jrieke/advanced-theming-examples)):
- [AirBnB](https://advanced-theming-airbnb.streamlit.app)  
- [Notion](https://advanced-theming-notion.streamlit.app)  
- [Spotify](https://advanced-theming-spotify.streamlit.app) 
- [Anthropic](https://advanced-theming-anthropic.streamlit.app)  
- [Anthropic Dark](https://advanced-theming-anthropic-dark.streamlit.app)  
- [OpenAI](https://advanced-theming-openai.streamlit.app)  
- [Apple](https://advanced-theming-apple.streamlit.app)  
"""

""

"""
## Flex layout :orange-badge[🎨 Design]

`st.container` is now a simplified flexbox:

```python
st.container(
    ...,
    horizontal: bool = False,
    horizontal_alignment: "left"|"center"|"right"|"distribute" = "left",
    vertical_alignment: "top"|"center"|"bottom"|"distribute" = "top",
    gap: "small"|"medium"|"large"|None = "small",
)
```

Plus, most elements now have `width` and `height`:

```python
st.line_chart(
    ..., 
    width: int|"stretch"|"content" = "stretch", 
    height: int|"stretch"|"content" = "content", 
)
```

##### Simple examples
"""

tab1, tab2, tab3, tab4 = st.tabs(["Horizontal container with buttons", "Centered text", "Gap + right aligned", "Distributed elements"])

with tab1:
    with st.echo():
        with st.container(horizontal=True):
            st.button("Button 1")
            st.button("Button 2")
            st.button("Button 3")

with tab2:
    with st.echo():
        with st.container(horizontal=True, horizontal_alignment="center"):
            st.markdown("This text is centered!", width="content")

with tab3:
    with st.echo():
        with st.container(gap="medium", horizontal_alignment="right"):
            st.button("Top button")
            st.button("Middle button")
            st.button("Bottom button")

with tab4:
    with st.echo():
        with st.container(horizontal=True, horizontal_alignment="distribute"):
            st.button("Left")
            st.button("Middle")
            st.button("Right")

"""
##### Complex example
"""
if st.button("📊 View dashboard example"):
    st.switch_page("pages/dashboard.py")

""

"""
## Advanced dataframes :green-badge[📊 Visualizations]

`st.dataframe` is one of our most used elements, and we made it much more powerful!
"""

""


editable = st.toggle("Make editable", False)

column_config = {
    "Company Name": st.column_config.TextColumn(pinned=True),
    "Logo": st.column_config.ImageColumn(width="small"),
    "Stock Price": st.column_config.NumberColumn(format="dollar"),
    "Market Cap": st.column_config.NumberColumn(format="compact"),
    "P/E Ratio": st.column_config.NumberColumn(format="%.1f"),
    "Dividend Yield (%)": st.column_config.ProgressColumn(
        format="%.2f%%", min_value=0, max_value=5
    ),
    "52W Change": st.column_config.NumberColumn(format="%.1f%%"),
    "Volume": st.column_config.BarChartColumn(y_min=0, y_max=70000000),
    "ESG Score": st.column_config.ProgressColumn(format="%d/100"),
    "Price Trend": st.column_config.AreaChartColumn(),
    "Performance Score": st.column_config.ProgressColumn(format="%d/100"),
    "Risk Level": st.column_config.NumberColumn(format="%d ⭐"),
    "Last Updated": st.column_config.DatetimeColumn(
        format="MMM DD, YYYY h:mm a"
    ),
    "Website": st.column_config.LinkColumn(),
    "Tags": st.column_config.MultiselectColumn(
        options=["Technology", "Devices", "Cloud", "Retail", "Ads", "Auto", "Social", "AI", "Semiconductors", "Finance", "Conglomerate"],
        color=["blue", "blue", "green", "yellow", "orange", "red", "violet", "blue", "green", "gray", "blue"],
    ),
}

if editable:
    st.data_editor(df, column_config=column_config)
else:
    st.dataframe(df, column_config=column_config)


"""
Highlights:

- 17 [column types](https://docs.streamlit.io/develop/api-reference/data/st.column_config) via `st.column_config`:
  ```python
  st.dataframe(
      ..., 
      column_config={
          "Logo": st.column_config.ImageColumn(),
          "Volume": st.column_config.BarChartColumn(y_min=0, y_max=70000000),
          "Market Cap": st.column_config.NumberColumn(format="compact"),
      },
  )
  ```
  
- Rich [editing](https://docs.streamlit.io/develop/api-reference/data/st.data_editor) via `st.data_editor`:
  ```python
  edited_data = st.data_editor(df)
  ```
- New UI controls: click on the :material/more_vert: menu of a column header!
- Supports Pandas, Polars, Dask, PyArrow, Snowpark, Modin, ...
- (Coming soon) Lazy loading from the backend or database
"""

""

"""
## Selections for charts & dataframes :green-badge[📊 Visualizations]

Create more interactive visualizations with `on_select="rerun"`:
"""

selection_type = st.segmented_control(
    "Selection examples", ["Chart", "Dataframe", "Map"], default="Chart", label_visibility="collapsed"
)

if selection_type == "Chart":
    
    df = px.data.gapminder()
    fig = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )

    with st.echo():
        event_data = st.plotly_chart(fig, on_select="rerun")
        
    "Return value:"
    st.write(event_data)

elif selection_type == "Dataframe":
    df_small = df[["Company Name", "Stock Price", "Tags"]]
    with st.echo():
        event_data = st.dataframe(
            df_small,
            on_select="rerun",
            selection_mode=["multi-row", "multi-column", "multi-cell"],
        )
    "Return value:"
    st.write(event_data)

elif selection_type == "Map":
    
    H3_HEX_DATA = [
        {"hex": "88283082b9fffff", "count": 10},
        {"hex": "88283082d7fffff", "count": 50},
        {"hex": "88283082a9fffff", "count": 100},
    ]
    df = pd.DataFrame(H3_HEX_DATA)
    
    deck = pdk.Deck(
        map_style="light",
        initial_view_state=pdk.ViewState(
            latitude=37.7749295,
            longitude=-122.4194155,
            zoom=11,
            bearing=0,
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                "H3HexagonLayer",
                df,
                id="MyHexLayer",
                pickable=True,
                stroked=True,
                filled=True,
                get_hexagon="hex",
                line_width_min_pixels=2,
                get_fill_color="[120, count > 50 ? 255 : 0, 255]",
            ),
            pdk.Layer(
                "LineLayer",
                "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-segments.json",
                id="BartLinesLayer",
                get_source_position="from.coordinates",
                get_target_position="to.coordinates",
                get_color="[inbound - outbound, 140, 0]",
                get_width=9,
                pickable=True,
            ),
        ]
    
    )
    with st.echo():
        event_data = st.pydeck_chart(deck, on_select="rerun")
        
    "Return value:"
    st.write(event_data)


""

"""
## Fragments :blue-badge[🏃‍♀️ Performance]

Fragments allow you to rerun only part of your app when certain widgets change, improving performance:
"""


if st.toggle("Enable fragment example", False):

    with st.echo():
        
        st.write("Above the fragment")
        
        @st.fragment
        def release_the_balloons():
            st.button("Release the balloons", help="Fragment rerun")
            st.balloons()

        with st.spinner("Inflating balloons..."):
            time.sleep(5)
            
        release_the_balloons()
        
        st.write("Below the fragment")
        st.button("Inflate more balloons (full rerun)")

""

"""
## Authentication :yellow-badge[🔐 Security]

Add login with Google, GitHub, or any other OAuth2 provider in a few lines of code!

In `.streamlit/secrets.toml`, add the app credentials:
    
```toml
[auth]
redirect_uri = "http://<app_url>/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

Then, use `st.login`, `st.logout`, and `st.user` in your app:
"""

with st.echo():
    if not st.user.is_logged_in:
        if st.button("Log in"):
            st.login()
    else:
        if st.button("Log out"):
            st.logout()
        st.write(f"Hello, {st.user.name}!")