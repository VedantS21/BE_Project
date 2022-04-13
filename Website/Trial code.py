"""
Trial code
# specify the primary menu definition

app = HydraApp(title='Sample Hydralit App',favicon="🐙")
  
#add all your application classes here
app.add_app("Small App", icon="🏠", app=form())
menu_data = [
    {'icon': "far fa-copy", 'label':"Pedict Disease"},
    {'icon': "far fa-copy", 'label':"Home Remedies & Diet"},
    {'icon': "far fa-copy", 'label':"My Profile"},
    {'icon': "far fa-copy", 'label':"Patient Form"},
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)
"""