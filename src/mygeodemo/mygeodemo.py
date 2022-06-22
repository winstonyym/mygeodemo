from ipyleaflet import Map, basemaps, basemap_to_tiles, Marker, LayersControl

class LeafMap(Map):
    """Class to extend ipyleaflet.Map class

    Added additional controls and default plotting parameters.

    Attributes
    ----------
    blah
    
    Methods
    -------
    blah

    """

    def __init__(self, **kwargs):
        if 'center' not in kwargs:
            kwargs['center'] = (1.3521, 103.8198)

        if 'zoom' not in kwargs:
            kwargs['zoom'] = 12

        super().__init__(**kwargs)
        
        dark_matter_layer = basemap_to_tiles(basemaps.CartoDB.DarkMatter)
        self.add_layer(dark_matter_layer)

        esri_layer = basemap_to_tiles(basemaps.Esri.NatGeoWorldMap);
        self.add_layer(esri_layer)

        marker = Marker(name='Location', location=kwargs['center'], draggable=False)
        self.add_layer(marker);

        control = LayersControl(position='topright')
        self.add_control(control)

        return 
        
def clean_text(text):
    """Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        Text to clean.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> clean_text("Early optimization is the root of all evil!")
    'early optimization is the root of all evil'
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

