import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from monstro import criar_monstro


class MonstroGUI:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.campos_visiveis = False
        self.carregar_widgets()

    def configurar_janela(self):
        self.root.title("Criador de Monstros 🐉")
        largura_janela = 1075
        altura_janela = 614
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_central = int((largura_tela - largura_janela) / 2)
        y_central = int((altura_tela - altura_janela) / 2)
        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_central}+{y_central}")
        self.root.resizable(False, False)

        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    def carregar_widgets(self):
        self.criar_titulo()
        self.criar_saida()
        self.carregar_botoes()

    def criar_titulo(self):
        title_frame = tk.Frame(self.root, bg="#2b2b2b", highlightbackground="#388E3C", highlightthickness=3)
        title_frame.place(relx=0.5, y=30, anchor="center", width=500, height=50)

        shadow = tk.Label(
            title_frame,
            text="Criador de Monstros 🐉",
            font=("Helvetica", 24, "bold"),
            fg="#1A1A1A",
            bg="#2b2b2b",
        )
        shadow.place(relx=0.505, rely=0.505, anchor="center")

        title = tk.Label(
            title_frame,
            text="Criador de Monstros 🐉",
            font=("Helvetica", 24, "bold"),
            fg="#FFD700",
            bg="#2b2b2b",
        )
        title.place(relx=0.5, rely=0.5, anchor="center")

    def criar_saida(self):
        self.output_frame = tk.Frame(self.root, bg="#2b2b2b", highlightthickness=2, highlightbackground="#388E3C")
        self.output_frame.place_forget()

        self.text_output = tk.Text(
            self.output_frame,
            font=("Courier", 14),
            width=90,
            height=11,
            state="disabled",
            bg="#2b2b2b",
            fg="#FFD700",
            highlightthickness=0,
        )
        self.text_output.pack(side="left", fill="both", expand=True)

        self.close_output_button = tk.Button(
            self.output_frame,
            text="✖",
            font=("Helvetica", 12, "bold"),
            bg="#2b2b2b",
            fg="#FFD700",
            bd=0,
            command=self.fechar_saida,
        )
        self.close_output_button.place(relx=1.0, rely=0.0, anchor="ne", x=-5, y=5)

    def criar_entradas(self):
        self.nome_label, self.nome_entry = self.criar_campo("Nome do Monstro", 0.35)
        self.tipo_label, self.tipo_entry = self.criar_campo("Tipo do Monstro", 0.42)
        self.forca_label, self.forca_entry = self.criar_campo("Nível de Força (1-100)", 0.49)
        self.habilidade_label, self.habilidade_entry = self.criar_campo("Habilidade Especial", 0.56)

        self.forca_entry.bind("<KeyRelease>", self.validar_forca)
        self.nome_entry.bind("<KeyRelease>", self.verificar_inputs)
        self.tipo_entry.bind("<KeyRelease>", self.verificar_inputs)
        self.habilidade_entry.bind("<KeyRelease>", self.verificar_inputs)

        self.criar_botao_confirmar()

    def criar_campo(self, texto, y_pos):
        label = tk.Label(
            self.root,
            text=texto,
            font=("Helvetica", 14),
            bg="#2b2b2b",
            fg="#FFD700",
        )
        label.place(relx=0.3, rely=y_pos, anchor="center")

        entry = tk.Entry(
            self.root,
            font=("Helvetica", 14),
            width=30,
            bg="#2b2b2b",
            fg="#FFD700",
            insertbackground="#FFD700",
            highlightthickness=2,
            highlightbackground="#388E3C",
            highlightcolor="#66BB6A",
        )
        entry.place(relx=0.6, rely=y_pos, anchor="center")

        return label, entry

    def validar_forca(self, event=None):
        valor = self.forca_entry.get().strip()
        if not valor.isdigit() or not (1 <= int(valor) <= 100):
            self.forca_entry.configure(bg="#FFCCCC")
        else:
            self.forca_entry.configure(bg="#2b2b2b")
        self.verificar_inputs()

    def criar_botao_confirmar(self):
        self.botao_criar = tk.Button(
            self.root,
            text="Criar Monstro",
            font=("Helvetica", 14),
            bg="#555555",
            fg="#AAAAAA",
            state="disabled",
            command=self.criar_monstro,
        )
        self.botao_criar.place(relx=0.5, rely=0.65, anchor="center")

    def verificar_inputs(self, event=None):
        nome = self.nome_entry.get().strip()
        tipo = self.tipo_entry.get().strip()
        forca = self.forca_entry.get().strip()
        habilidade = self.habilidade_entry.get().strip()

        if nome and tipo and forca.isdigit() and 1 <= int(forca) <= 100 and habilidade:
            self.botao_criar.config(bg="#1B5E20", fg="#FFD700", state="normal")
        else:
            self.botao_criar.config(bg="#555555", fg="#AAAAAA", state="disabled")

    def carregar_botoes(self):
        self.icon_add = ImageTk.PhotoImage(Image.open("assets/add.png").resize((50, 50)))
        self.icon_exit = ImageTk.PhotoImage(Image.open("assets/exit.png").resize((50, 50)))

        self.create_hover_button(self.root, self.icon_add, "Adicionar Monstro", self.mostrar_entradas, 0.35)
        self.create_hover_button(self.root, self.icon_exit, "Sair", self.sair, 0.65)

    def create_hover_button(self, root, icon, tooltip_text, command, relx_position):
        button = tk.Button(
            root,
            image=icon,
            command=command,
            bg="#0D3A16",
            activebackground="#1B5E20",
            bd=0,
            relief="flat",
            highlightthickness=0,
        )
        button.place(relx=relx_position, rely=0.9, anchor="center")

        tooltip = tk.Label(
            root,
            text=tooltip_text,
            font=("Helvetica", 10, "italic"),
            bg="#2b2b2b",
            fg="#FFD700",
            relief="solid",
            borderwidth=1,
            padx=5,
            pady=2,
        )
        tooltip.place_forget()

        def on_enter(e):
            button.config(bg="#1B5E20", relief="raised")
            tooltip.place(relx=relx_position, rely=0.85, anchor="center")

        def on_leave(e):
            button.config(bg="#0D3A16", relief="flat")
            tooltip.place_forget()

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def exibir_saida(self, texto):
        self.output_frame.place(relx=0.5, rely=0.6, anchor="center")
        self.text_output.configure(state="normal")
        self.text_output.delete("1.0", tk.END)

        mensagem_formatada = (
            f"\n{'='*50}\n"
            f"✨ **Parabéns, seu monstro foi criado!** ✨\n"
            f"{'-'*50}\n"
            f"🦴 **Nome:** {self.nome_entry.get().strip()}\n"
            f"🐾 **Tipo:** {self.tipo_entry.get().strip()}\n"
            f"💪 **Força:** {self.forca_entry.get().strip()}\n"
            f"🌀 **Habilidade Especial:** {self.habilidade_entry.get().strip()}\n"
            f"{'='*50}\n"
            f"🌟 Agora ele está pronto para ajudá-lo em sua jornada! 🌟\n"
        )

        self.text_output.insert(tk.END, mensagem_formatada)
        self.text_output.configure(state="disabled")

    def fechar_saida(self):
        self.output_frame.place_forget()

    def mostrar_entradas(self):
        if not self.campos_visiveis:
            self.criar_entradas()
            self.campos_visiveis = True

    def criar_monstro(self):
        nome = self.nome_entry.get().strip()
        tipo = self.tipo_entry.get().strip()
        forca = self.forca_entry.get().strip()
        habilidade = self.habilidade_entry.get().strip()

        descricao = criar_monstro(nome, tipo, forca, habilidade)
        self.limpar_campos()
        self.exibir_saida(descricao)

    def limpar_campos(self):
        self.nome_label.place_forget()
        self.nome_entry.place_forget()
        self.tipo_label.place_forget()
        self.tipo_entry.place_forget()
        self.forca_label.place_forget()
        self.forca_entry.place_forget()
        self.habilidade_label.place_forget()
        self.habilidade_entry.place_forget()
        self.botao_criar.place_forget()
        self.campos_visiveis = False

    def sair(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MonstroGUI(root)
    root.mainloop()
