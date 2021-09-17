import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests

# password_attempt = st.text_input('Please Enter The Password')
# if password_attempt != 'example_password':
#      st.write('Write the Password above')
#      st.stop()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_jhu1lqdz.json')
st_lottie(lottie_airplane, speed=1, height=200, key="initial")
st.title('Quantum Theory')
st.write('by Me')
st.subheader('Question 1: ')
'''
1.1 The work function of barium and tungsten are 2.5 eV and 4.2 eV, respectively. Check whether
these materials are useful in a photocell, which is to be used to detect visible light.
'''

'''
Solution. The wavelength l of visible light is in the range 4000–7000 Å. Then,
'''

st.latex(r'Energy\hspace{0.1cm}of\hspace{0.1cm}4000\hspace{0.1cm}\mathop A\limits^o \hspace{0.1cm}light = \frac{{hc}}{\lambda } = \frac{{(6.626 \times {{10}^{ - 34}}Js)(3 \times {{10}^8}m/s)}}{{(4000 \times {{10}^{ - 10}}m)(1.6 \times {{10}^{ - 19}}J/eV)}} = 3.106eV')
st.latex(r'Energy\hspace{0.1cm}of\hspace{0.1cm}7000\hspace{0.1cm}\mathop A\limits^o \hspace{0.1cm}light = \frac{{hc}}{\lambda } = \frac{{(6.626 \times {{10}^{ - 34}}Js)(3 \times {{10}^8}m/s)}}{{(7000 \times {{10}^{ - 10}}m)(1.6 \times {{10}^{ - 19}}J/eV)}} = 1.77eV')

'''
The work function of tungsten is 4.2 eV, which is more than the energy range of visible light. Hence,
barium is the only material useful for the purpose.
'''
st.latex(r'\\')
st.latex(r'\\')
'''
2.18 Normalize the wave function ψ(x) = A exp (–ax^2
), A and a are constants, over the domain
– ∞ ≤ x ≤ ∞.

Solution. Taking A as the normalization constant, we get
'''
st.latex(r'{A^2}\int_{ - \infty }^\infty  {{\psi ^*}\psi dx = } {A^2}\int_{ - \infty }^\infty  {\exp ( - 2a{x^2})dx = 1}')
st.latex(r'\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}dx, \hspace{0.5cm}} \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2} - 2a{y^2}}}dxdy} ,\hspace{0.5cm}} \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}{e^{ - 2a{y^2}}}dxdy} ,} ')
st.latex(r'\int_{ - \infty }^\infty  {{e^{ - 2a{y^2}}}dy\int_{ - \infty }^\infty  {{e^{ - 2a{x^2}}}dx,\hspace{0.5cm}} I} \int_{ - \infty }^\infty  {{e^{ - 2a{y^2}}}dy = {I^2},} ')
st.latex(r'{I^2} = \int_{ - \infty }^\infty  {\int_{ - \infty }^\infty  {{e^{ - 2a{x^2} - 2a{y^2}}}dxdy} ,\hspace{0.5cm}} \int_0^\infty  {\int_0^{2\pi } {{e^{ - 2a{r^2}}}rd\theta d} r,} ')
st.latex(r'2\pi \int_0^\infty  {{e^{ - 2a{r^2}}}rdr,\hspace{0.5cm}u = }  - 2a{r^2},\hspace{0.5cm}du =  - 4ardr')
st.latex(r' - \frac{{2\pi }}{{4a}}\left. {{e^{ - 2a{r^2}}}} \right|_0^\infty  = \frac{\pi }{{2a}},\hspace{0.5cm}\therefore\hspace{0.5cm} I = \sqrt {\frac{\pi }{{2a}}} ')
st.latex(r'{A^2} = \frac{1}{{\sqrt {\frac{\pi }{{2a}}} }},\hspace{0.5cm}A = {\left( {\frac{{2a}}{\pi }} \right)^{1/4}}')
st.latex(r'\psi (x) = {\left( {\frac{{2a}}{\pi }} \right)^{1/4}}\exp ( - a{x^2})')

st.latex(r'\\')
st.latex(r'\\')

'''
2.19 A particle constrained to move along the x-axis in the domain 0 ≤ x ≤ L has a wave function
ψ(x) = sin (npx/L), where n is an integer. Normalize the wave function and evaluate the expectation
value of its momentum.
'''
'''
Solution. The normalization condition gives
'''
st.latex(r'{N^2}\int_0^L {{{\sin }^2}\frac{{n\pi x}}{L}dx = 1} ')
st.latex(r'{N^2}\int_0^L {\frac{1}{2}\left( {1 - \cos \frac{{2n\pi x}}{L}} \right)dx = 1} ')
st.latex(r'{N^2}\left[ {\frac{1}{2}\int_0^L {dx - \frac{1}{2}\int_0^L {\cos \frac{{2n\pi x}}{L}} dx} } \right] = 1,\hspace{1cm}{N^2}\left[ {\frac{1}{2}L - \frac{1}{2}\left( {\frac{L}{{2n\pi }}} \right)\sin \left. {\frac{{2n\pi x}}{L}} \right|_0^L} \right]')
st.latex(r'\frac{{{N^2}L}}{2} = 1,\hspace{1cm}N = \sqrt {\frac{2}{L}}')
'''
The normalized wave function is √(2/L) sin[(nπx)/L]. So,
'''
st.latex(r'\left\langle {{p_x}} \right\rangle  = \int_0^L {{\psi ^*}\left( { - i\hbar \frac{d}{{dx}}} \right)} \psi dx')
st.latex(r' \int_0^L {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right) \cdot \left( { - i\hbar \frac{d}{{dx}}\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right)} \right)} dx')
st.latex(r'\frac{d}{{dx}}\left( {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right)} \right) = \sqrt {\frac{2}{L}} \frac{{n\pi }}{L}\cos \frac{{n\pi x}}{L}')
st.latex(r'\int_0^L {\sqrt {\frac{2}{L}} \sin \left( {\frac{{n\pi x}}{L}} \right) \cdot \left( { - i\hbar \sqrt {\frac{2}{L}} \frac{{n\pi }}{L}\cos \frac{{n\pi x}}{L}} \right)} dx')
st.latex(r' - i\hbar \frac{2}{L}\frac{{n\pi }}{L}\int_0^L {\sin \left( {\frac{{n\pi x}}{L}} \right)} \cos \left( {\frac{{n\pi x}}{L}} \right)dx')
st.latex(r'\sin 2A = 2\sin A\cos A,\hspace{1cm} - i\hbar \frac{{2n\pi }}{{{L^2}}}\left( {\frac{1}{2}} \right)\int_0^L {\sin \frac{{2n\pi x}}{L}dx} ')
st.latex(r' - i\hbar \frac{{n\pi }}{{{L^2}}}\int_0^L {\sin \frac{{2n\pi x}}{L}dx}  = 0')

