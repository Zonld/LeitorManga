from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.card import MDCard
from kivy.core.window import Window
import os

class LeitorApp(MDApp):
    current_page = 0
    pages = []
    chapter_directories = []
    read_chapters = {}  
    chapter_buttons = {} 
    current_chapter_index = 0 
    current_manga = "" 

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        Window.size = (700, 890)
        self.title = 'Leitor de Mangás'
        self.layout_inicial = self.criar_layout_inicial()
        return self.layout_inicial

    def criar_layout_inicial(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        card1 = MDCard(size_hint=(1, None), height=400, orientation='horizontal', padding=20, spacing=35,
                    md_bg_color=(0.2, 0.2, 0.2, 1), radius=[15, 15, 15, 15])

        card_content1 = MDBoxLayout(orientation='horizontal', size_hint=(1, 1))

        imagem1 = Image(source='capas/onepiece.webp', allow_stretch=True, size_hint=(None, 1), width=230)

        right_content1 = MDBoxLayout(orientation='vertical', size_hint=(1, 1), padding=(10, 0, 0, 0), spacing=10)
        texto1 = MDLabel(
            text="One Piece", size_hint_y=None, height=30, halign="left",
            theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style='H5', bold=True
        )
        novo_texto1 = MDLabel(
            text="Gol D. Roger era conhecido como o Rei dos Piratas, ele conquistou tudo na vida fortuna, fama e poder. Passados 22 anos, o garoto Monkey D. Luffy, usuário da Gomu Gomu no Mi, parte em busca do seu sonho, achar o One Piece e se tornar o Rei dos Piratas, que é o título da pessoa que vai conquistar o mundo. Luffy terá de juntar uma tripulação forte no East Blue, o mar mais fraco de todos. Aparecerão muitos inimigos poderosos em seu caminho.",
            size_hint_y=None, height=250, halign="left",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )

        botao_ler_capitulos1 = MDRaisedButton(text="Ler Capítulos", size_hint=(1, None), height=50, on_release=self.ir_para_capitulos)

        right_content1.add_widget(texto1)
        right_content1.add_widget(novo_texto1)
        right_content1.add_widget(botao_ler_capitulos1)

        card_content1.add_widget(imagem1)
        card_content1.add_widget(right_content1)

        card1.add_widget(card_content1)

        card2 = MDCard(size_hint=(1, None), height=400, orientation='horizontal', padding=20, spacing=35,
                    md_bg_color=(0.2, 0.2, 0.2, 1), radius=[15, 15, 15, 15])

        card_content2 = MDBoxLayout(orientation='horizontal', size_hint=(1, 1))

        imagem2 = Image(source='capas/hunter.webp', allow_stretch=True, size_hint=(None, 1), width=230)

        right_content2 = MDBoxLayout(orientation='vertical', size_hint=(1, 1), padding=(10, 0, 0, 0), spacing=10)
        texto2 = MDLabel(
            text="Hunter x Hunter", size_hint_y=None, height=30, halign="left",
            theme_text_color="Custom", text_color=(1, 1, 1, 1), font_style='H5', bold=True
        )
        novo_texto2 = MDLabel(
            text="Em Hunter x Hunter, o jovem Gon se apega ao legado de seu desconhecido pai e sonha em se tornar um Hunter, um caçador de tesouros e artefatos místicos. Ao descobrir que o pai está vivo, ele sai em uma missão para encontrá-lo enquanto tenta se tornar um Hunter profissional. Ele conhece Killua, Kurapika e Leorio, que compartilham as mesmas aspirações que ele e juntos embarcam em perigosas e emocionantes aventuras.",
            size_hint_y=None, height=250, halign="left",
            theme_text_color="Custom", text_color=(1, 1, 1, 1)
        )

        botao_ler_capitulos2 = MDRaisedButton(text="Ler Capítulos", size_hint=(1, None), height=50, on_release=self.ir_para_capitulos2)

        right_content2.add_widget(texto2)
        right_content2.add_widget(novo_texto2)
        right_content2.add_widget(botao_ler_capitulos2)

        card_content2.add_widget(imagem2)
        card_content2.add_widget(right_content2)

        card2.add_widget(card_content2)

        layout.add_widget(card1)
        layout.add_widget(card2)

        return layout

    def ir_para_capitulos(self, instance):
        self.current_manga = "one_piece" 
        self.chapter_directories = [d for d in os.listdir('capitulos') if os.path.isdir(os.path.join('capitulos', d))]
        self.layout_principal = self.criar_layout_principal()
        self.root.clear_widgets()
        self.root.add_widget(self.layout_principal)

    def ir_para_capitulos2(self, instance):
        self.current_manga = "hunter_x_hunter" 
        self.chapter_directories = [d for d in os.listdir('capitulos2') if os.path.isdir(os.path.join('capitulos2', d))]
        self.layout_principal = self.criar_layout_principal()
        self.root.clear_widgets()
        self.root.add_widget(self.layout_principal)

    def criar_layout_principal(self):
        layout = MDBoxLayout(orientation='vertical', padding=0, spacing=0)

        botao_voltar_inicial = MDRaisedButton(
            text="Voltar para Página Inicial",
            pos_hint = {"center_x": 0.5, "top": 1},
            size_hint=(0.3, 0.05),
            height=50,
            on_release=self.voltar_menu 
        )
        
        layout.add_widget(botao_voltar_inicial)

        texto = MDBoxLayout(orientation='horizontal', size_hint=(1, 1), height=100, padding=20, spacing=50)

        layout.add_widget(texto)

        def extract_number(chapter_name):
            return int(chapter_name.split(' - ')[0]) 

        self.chapter_directories.sort(key=extract_number)

        for chapter in self.chapter_directories:
            chapter_layout = MDBoxLayout(orientation='horizontal', size_hint=(1, None), height=50, padding=20)

            botao_capitulo = MDRaisedButton(
                text=chapter,
                on_release=lambda instance, chap=chapter: self.ler_capitulo(chap),
                size_hint=(0.5, 3),
                md_bg_color=(0.2, 0.2, 0.2, 1),
                text_color=(1, 1, 1, 1),
                halign='left'
            )

            if self.read_chapters.get(chapter, False):
                botao_capitulo.md_bg_color = (0.3, 0.3, 0.3, 1)
            self.chapter_buttons[chapter] = botao_capitulo

            checkbox = MDCheckbox(
                active=self.read_chapters.get(chapter, False), 
                size_hint=(None, 3), 
                size=(48, 48),
                color=(0.2, 0.2, 0.2, 0.5),
                color_active=(0.5, 0.5, 0.5, 0.5)
            )

            def create_checkbox_callback(chap, button):
                return lambda instance, value: self.marcar_capitulo_lido(chap, value, button)

            checkbox.bind(active=create_checkbox_callback(chapter, botao_capitulo))

            chapter_layout.add_widget(checkbox)
            chapter_layout.add_widget(botao_capitulo)
            layout.add_widget(chapter_layout)

        return layout

    def marcar_capitulo_lido(self, chapter, is_read, botao_capitulo=None):
        self.read_chapters[chapter] = is_read

        if botao_capitulo is None:
            botao_capitulo = self.chapter_buttons.get(chapter)

        if botao_capitulo:
            if is_read:
                botao_capitulo.md_bg_color = (0.3, 0.3, 0.3, 1)
            else:
                botao_capitulo.md_bg_color = (0.2, 0.2, 0.2, 1)

    def ler_capitulo(self, chapter):
        self.current_page = 0
        self.pages = []

        self.current_chapter_index = self.chapter_directories.index(chapter)

        chapter_path = os.path.join('capitulos' if self.current_manga == "one_piece" else 'capitulos2', chapter)

        if not os.path.exists(chapter_path):
            print(f"O caminho do capítulo não existe: {chapter_path}")
            return

        self.pages = [
            os.path.join(chapter_path, f)
            for f in os.listdir(chapter_path)
            if f.lower().endswith(('.jpg', '.png'))
        ]

        if not self.pages:
            print(f"Nenhuma página encontrada no capítulo: {chapter}")
            return

        self.layout_leitura = self.criar_layout_leitura()
        self.root.clear_widgets()
        self.root.add_widget(self.layout_leitura)

    def ler_proximo_capitulo(self):
        if self.current_chapter_index < len(self.chapter_directories) - 1:
            self.current_chapter_index += 1
            next_chapter = self.chapter_directories[self.current_chapter_index]
            self.ler_capitulo(next_chapter)

    def criar_layout_leitura(self):
        layout = MDBoxLayout(orientation='vertical', padding=0, spacing=0)

        barra_superior = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10, spacing=10, md_bg_color=(0.3, 0.3, 0.3, 1), radius=[3, 3, 3, 3]) 

        botao_voltar_capitulos = MDRaisedButton(
            text="Voltar Para o Menu de Capitulos",
            on_release=self.voltar_para_capitulos,
            size_hint=(0.3, 1),
            size=(200, 50)
        )
        barra_superior.add_widget(botao_voltar_capitulos)

        self.page_input = MDTextField(
            text=str(self.current_page + 1),
            hint_text="",
            input_filter="int",
            size_hint=(0.05, 1),
            halign="center",
            multiline=False
        )
        barra_superior.add_widget(self.page_input)

        total_paginas_label = MDLabel(
            text=f"/ {len(self.pages)}",
            halign="center",
            size_hint=(0.06, 1),
            width=80
        )
        barra_superior.add_widget(total_paginas_label)

        layout.add_widget(barra_superior)

        botao_ir_pagina = MDRaisedButton(
            text="Buscar",
            on_release=self.ir_para_pagina_por_input,
            size_hint=(0.3, 1)
        )
        barra_superior.add_widget(botao_ir_pagina)

        self.imagem_pagina = Image(source=self.pages[self.current_page], allow_stretch=True, size_hint=(1, 1))
        layout.add_widget(self.imagem_pagina)

        navigation_layout = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10, spacing=10, md_bg_color=(0.3, 0.3, 0.3, 1), radius=[3, 3, 3, 3])

        botao_anterior = MDRaisedButton(
            text="Página Anterior",
            on_release=self.pagina_anterior,
            size_hint=(1, 1),
            size=(150, 50)
        )
        navigation_layout.add_widget(botao_anterior)

        botao_proxima = MDRaisedButton(
            text="Próxima Página",
            on_release=self.pagina_proxima,
            size_hint=(1, 1),
            size=(150, 50)
        )
        navigation_layout.add_widget(botao_proxima)

        layout.add_widget(navigation_layout)

        return layout

    def voltar_para_capitulos(self, instance):
        self.root.clear_widgets()
        self.layout_principal = self.criar_layout_principal() 
        self.root.add_widget(self.layout_principal)

    def voltar_menu(self, instance):
        self.root.clear_widgets()
        self.layout_inicial = self.criar_layout_inicial() 
        self.root.add_widget(self.layout_inicial)

    def ir_para_pagina(self, instance):
            page_number = int(self.page_input.text) - 1 
            if 0 <= page_number < len(self.pages):
                self.current_page = page_number
                self.atualizar_pagina()

    def pagina_anterior(self, instance):
        if self.current_page > 0:
            self.current_page -= 1
            self.atualizar_pagina()

    def pagina_proxima(self, instance):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.atualizar_pagina()
        else:
            self.marcar_capitulo_lido(self.chapter_directories[self.current_chapter_index], True)
            if self.current_chapter_index < len(self.chapter_directories) - 1:
                self.ler_proximo_capitulo()
            else:
                print("Você terminou todos os capítulos!")

    def ir_para_pagina_por_input(self, instance):
        try:
            page_number = int(self.page_input.text) - 1 
            if 0 <= page_number < len(self.pages):
                self.current_page = page_number
                self.atualizar_pagina()
            else:
                self.page_input.text = str(self.current_page + 1)
        except ValueError:
            self.page_input.text = str(self.current_page + 1)
            

    def atualizar_pagina(self):
        self.imagem_pagina.source = self.pages[self.current_page]
        self.page_input.text = str(self.current_page + 1)

LeitorApp().run()