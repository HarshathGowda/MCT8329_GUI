import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTabWidget, QScrollArea, QGroupBox,
    QCheckBox, QComboBox, QFrame, QGridLayout, QSizePolicy,
    QSpacerItem, QSpinBox, QLineEdit
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter, QBrush, QPen

from registers_data import REGISTERS, REGISTER_ORDER

# ── Styles ───────────────────────────────────────────────────────────────────

DARK_BG      = "#F4F5F7"
PANEL_BG     = "#FFFFFF"
CARD_BG      = "#F7F8FA"
ACCENT       = "#0072CE"
ACCENT2      = "#5A4FCF"
RESERVED_CLR = "#D8DCE3"
TEXT_PRIMARY = "#1F2430"
TEXT_MUTED   = "#6B7280"
GREEN        = "#16A37A"
ORANGE       = "#E07B39"
RED_ACCENT   = "#D6294B"

STYLE_SHEET = f"""
QMainWindow, QWidget {{
    background-color: {DARK_BG};
    color: {TEXT_PRIMARY};
    font-family: 'Segoe UI', 'Inter', sans-serif;
}}

QTabWidget::pane {{
    border: 1px solid #D8DCE3;
    background: {PANEL_BG};
    border-radius: 6px;
}}

QTabBar::tab {{
    background: {CARD_BG};
    color: {TEXT_MUTED};
    padding: 8px 18px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    margin-right: 3px;
    font-size: 12px;
    font-weight: 600;
    border: 1px solid #D8DCE3;
    border-bottom: none;
}}

QTabBar::tab:selected {{
    background: {PANEL_BG};
    color: {ACCENT};
    border-bottom: 2px solid {ACCENT};
}}

QTabBar::tab:hover:!selected {{
    color: {TEXT_PRIMARY};
    background: #EDEFF3;
}}

QPushButton#registerBtn {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {ACCENT2}, stop:1 {ACCENT});
    color: #0D1117;
    border: none;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.3px;
    text-align: left;
}}

QPushButton#registerBtn:hover {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #4A3FBF, stop:1 #1B8FE0);
}}

QPushButton#registerBtn:pressed {{
    padding: 11px 15px 9px 17px;
}}

QPushButton#copyBtn, QPushButton#resetBtn {{
    background: {CARD_BG};
    color: {ACCENT};
    border: 1px solid {ACCENT};
    border-radius: 6px;
    padding: 7px 18px;
    font-size: 11px;
    font-weight: 600;
}}

QPushButton#copyBtn:hover, QPushButton#resetBtn:hover {{
    background: rgba(0, 114, 206, 0.12);
}}

QGroupBox {{
    border: 1px solid #D8DCE3;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 10px;
    background: {CARD_BG};
    font-weight: 600;
    font-size: 11px;
    color: {TEXT_MUTED};
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
    color: {ACCENT};
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}}

QCheckBox {{
    color: {TEXT_PRIMARY};
    spacing: 8px;
    font-size: 13px;
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 2px solid #D8DCE3;
    background: {PANEL_BG};
}}

QCheckBox::indicator:checked {{
    background: {ACCENT};
    border-color: {ACCENT};
    image: none;
}}

QCheckBox::indicator:hover {{
    border-color: {ACCENT};
}}

QComboBox {{
    background: {PANEL_BG};
    border: 1px solid #D8DCE3;
    border-radius: 5px;
    padding: 8px 12px;
    color: {TEXT_PRIMARY};
    font-size: 14px;
    min-width: 260px;
    min-height: 18px;
}}

QComboBox:disabled {{
    color: {TEXT_MUTED};
    background: {RESERVED_CLR};
}}

QComboBox::drop-down {{
    border: none;
    padding-right: 8px;
}}

QComboBox QAbstractItemView {{
    background: {CARD_BG};
    border: 1px solid #D8DCE3;
    color: {TEXT_PRIMARY};
    selection-background-color: rgba(0, 114, 206,0.18);
    font-size: 30px;
    outline: none;
}}

QComboBox QAbstractItemView::item {{
    min-height: 44px;
    padding: 6px 16px;
}}

QSpinBox {{
    background: {PANEL_BG};
    border: 1px solid #D8DCE3;
    border-radius: 5px;
    padding: 5px 8px;
    color: {TEXT_PRIMARY};
    font-size: 12px;
    min-width: 140px;
}}

QSpinBox:disabled {{
    color: {TEXT_MUTED};
    background: {RESERVED_CLR};
}}

QLineEdit#searchBox {{
    background: {PANEL_BG};
    border: 1px solid #D8DCE3;
    border-radius: 6px;
    padding: 8px 12px;
    color: {TEXT_PRIMARY};
    font-size: 13px;
}}

QLineEdit#searchBox:focus {{
    border: 1px solid {ACCENT};
}}

QScrollArea {{
    border: none;
    background: transparent;
}}

QScrollBar:vertical {{
    background: {PANEL_BG};
    width: 8px;
    border-radius: 4px;
}}

QScrollBar::handle:vertical {{
    background: #D8DCE3;
    border-radius: 4px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background: {ACCENT};
}}

QLabel#headerLabel {{
    font-size: 22px;
    font-weight: 700;
    color: {TEXT_PRIMARY};
    letter-spacing: 0.5px;
}}

QLabel#subLabel {{
    font-size: 12px;
    color: {TEXT_MUTED};
}}

QLabel#hexValue {{
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 20px;
    font-weight: 700;
    color: {ACCENT};
    background: {CARD_BG};
    border: 1px solid #D8DCE3;
    border-radius: 6px;
    padding: 8px 18px;
}}

QFrame#separator {{
    background: #D8DCE3;
    max-height: 1px;
}}

QLineEdit#hexInput {{
    background: #FFFFFF;
    border: 1.5px solid {ACCENT2};
    border-radius: 6px;
    padding: 6px 10px;
    color: {ACCENT};
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    font-weight: 700;
}}

QLineEdit#hexInput:focus {{
    border: 1.5px solid {ACCENT};
}}

QPushButton#submitBtn {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 {ACCENT2}, stop:1 {ACCENT});
    color: #0D1117;
    border: none;
    border-radius: 6px;
    padding: 7px 14px;
    font-size: 12px;
    font-weight: 700;
}}

QPushButton#submitBtn:hover {{
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #4A3FBF, stop:1 #1B8FE0);
}}

QPushButton#submitBtn:pressed {{
    padding: 8px 13px 6px 15px;
}}
"""


# ── Bit-map visualizer widget (interactive, clickable) ───────────────────────

class BitMapWidget(QWidget):
    """
    32-cell bit visualiser.  Click a non-reserved cell to toggle that bit.
    Emits bit_toggled(bit_index 0-31, new_value 0|1) so the tab can update
    field widgets.  Hover highlight shows which bit is under the cursor.
    """
    bit_toggled = pyqtSignal(int, int)   # (bit_index, new_value)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(70)
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)
        self._values   = [0] * 32   # 0=clear, 1=set, 2=reserved
        self._reserved = [False] * 32
        self._hovered  = -1

    def update_values(self, fields_state):
        """fields_state: list of (field_def, current_int_value)"""
        self._values   = [0] * 32
        self._reserved = [False] * 32
        for field, val in fields_state:
            hi, lo = field["bits"]
            if field["type"] == "reserved":
                for b in range(lo, hi + 1):
                    self._values[b]   = 2
                    self._reserved[b] = True
            else:
                for b in range(lo, hi + 1):
                    bit_pos = b - lo
                    self._values[b] = (val >> bit_pos) & 1
        self.update()

    def _col_of(self, x):
        """Column index (0=leftmost=bit31) at pixel x, or -1."""
        cell = self.width() / 32
        col  = int(x / cell)
        return col if 0 <= col <= 31 else -1

    def _bit_of(self, x):
        col = self._col_of(x)
        return (31 - col) if col >= 0 else -1

    def mouseMoveEvent(self, event):
        b = self._bit_of(event.x())
        if b != self._hovered:
            self._hovered = b
            self.update()

    def leaveEvent(self, event):
        self._hovered = -1
        self.update()

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        b = self._bit_of(event.x())
        if b < 0 or self._reserved[b]:
            return
        new_val = 0 if self._values[b] == 1 else 1
        self._values[b] = new_val
        self.update()
        self.bit_toggled.emit(b, new_val)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w   = self.width()
        cell = w / 32
        h   = self.height()
        cell_h = h - 22           # leave room for bit-number labels below

        for i in range(32):
            bit_idx = 31 - i
            v       = self._values[bit_idx]
            is_hov  = (bit_idx == self._hovered and not self._reserved[bit_idx])

            if v == 2:
                bg = QColor(RESERVED_CLR)
                fg = QColor(TEXT_MUTED)
            elif v == 1:
                bg = QColor("#2B8FE0") if is_hov else QColor(ACCENT)
                fg = QColor("#0D1117")
            else:
                bg = QColor("#E3ECFB") if is_hov else QColor(PANEL_BG)
                fg = QColor(TEXT_MUTED)

            x  = int(i * cell) + 1
            bw = max(int(cell) - 2, 4)

            # cell background
            painter.setBrush(QBrush(bg))
            border_col = QColor(ACCENT) if is_hov else QColor("#D8DCE3")
            painter.setPen(QPen(border_col, 1))
            painter.drawRoundedRect(x, 4, bw, cell_h, 3, 3)

            # 0/1 label inside cell
            if v != 2:
                painter.setPen(QPen(fg))
                painter.setFont(QFont("Consolas", 7, QFont.Bold))
                painter.drawText(x, 4, bw, cell_h, Qt.AlignCenter, str(v))

            # bit-number label below every 4th and bit 31
            if bit_idx % 4 == 0 or bit_idx == 31:
                painter.setPen(QPen(QColor(TEXT_MUTED)))
                painter.setFont(QFont("Consolas", 7))
                painter.drawText(int(x), h - 1, str(bit_idx))


# ── Field row widget ──────────────────────────────────────────────────────────

class FieldRow(QWidget):
    changed = pyqtSignal()

    def __init__(self, field, parent=None):
        super().__init__(parent)
        self.field = field
        self._value = field["reset"]
        self._build_ui()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(12)

        hi, lo = self.field["bits"]
        bit_label = QLabel(f"[{hi}:{lo}]" if hi != lo else f"[{hi}]")
        bit_label.setFont(QFont("Consolas", 10, QFont.Bold))
        bit_label.setStyleSheet(f"color: {ACCENT2}; min-width: 54px;")
        layout.addWidget(bit_label)

        # field name
        name = self.field["name"]
        if name.startswith("RESERVED"):
            name = "RESERVED"
        name_lbl = QLabel(name)
        name_lbl.setFont(QFont("Segoe UI", 10, QFont.Bold))
        is_reserved = self.field["type"] == "reserved"
        name_lbl.setStyleSheet(
            f"color: {TEXT_MUTED};" if is_reserved else f"color: {TEXT_PRIMARY};"
        )
        name_lbl.setMinimumWidth(190)
        name_lbl.setWordWrap(True)
        layout.addWidget(name_lbl)

        # description
        desc_lbl = QLabel(self.field["description"])
        desc_lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px;")
        desc_lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        desc_lbl.setWordWrap(True)
        desc_lbl.setMaximumWidth(420)
        layout.addWidget(desc_lbl)

        # sub-selection widget
        self.sub_widget = None
        width = hi - lo + 1
        max_val = (1 << width) - 1

        if self.field["type"] in ("combo", "toggle") and self.field["options"]:
            self.sub_widget = QComboBox()
            self.sub_widget.view().setMinimumWidth(600)
            for opt in self.field["options"]:
                self.sub_widget.addItem(opt)
            # Map combobox index -> actual bit value (options are sorted by code,
            # but a sparse/non-sequential option set still needs explicit mapping)
            self._option_values = []
            for opt in self.field["options"]:
                code_str = opt.split("h", 1)[0]
                try:
                    self._option_values.append(int(code_str, 16))
                except ValueError:
                    self._option_values.append(0)
            reset_idx = 0
            if self.field["reset"] in self._option_values:
                reset_idx = self._option_values.index(self.field["reset"])
            self.sub_widget.setCurrentIndex(reset_idx)
            self.sub_widget.currentIndexChanged.connect(self._on_combo_changed)
            layout.addWidget(self.sub_widget)

        elif self.field["type"] == "raw":
            self.sub_widget = QSpinBox()
            self.sub_widget.setRange(0, max_val if max_val < 2_000_000_000 else 2_000_000_000)
            self.sub_widget.setValue(self.field["reset"])
            self.sub_widget.setDisplayIntegerBase(10)
            self.sub_widget.valueChanged.connect(self._on_spin_changed)
            layout.addWidget(self.sub_widget)

        elif self.field["type"] == "reserved":
            rsv = QLabel("Reserved")
            rsv.setStyleSheet(
                f"color: {TEXT_MUTED}; background: {RESERVED_CLR};"
                "border-radius:4px; padding:3px 10px; font-size:11px;"
            )
            layout.addWidget(rsv)

        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def _on_combo_changed(self, idx):
        if 0 <= idx < len(self._option_values):
            self._value = self._option_values[idx]
        self.changed.emit()

    def _on_spin_changed(self, val):
        self._value = val
        self.changed.emit()

    def get_value(self):
        if self.field["type"] == "reserved":
            return 0
        return self._value

    def reset(self):
        self._value = self.field["reset"]
        if isinstance(self.sub_widget, QComboBox):
            reset_idx = 0
            if self.field["reset"] in getattr(self, "_option_values", []):
                reset_idx = self._option_values.index(self.field["reset"])
            self.sub_widget.setCurrentIndex(reset_idx)
        elif isinstance(self.sub_widget, QSpinBox):
            self.sub_widget.setValue(self.field["reset"])
        self.changed.emit()


# ── Register tab ──────────────────────────────────────────────────────────────

class RegisterTab(QWidget):
    def __init__(self, acronym, reg_def, parent=None):
        super().__init__(parent)
        self.acronym  = acronym
        self.reg_def  = reg_def
        self._loading = False   # guard against recursive update loops
        self._build_ui()

    # ── UI construction ────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        # ── header row ─────────────────────────────────────────────────────
        hdr = QHBoxLayout()
        title = QLabel(self.acronym)
        title.setObjectName("headerLabel")
        hdr.addWidget(title)

        offset_lbl = QLabel(
            f"Offset = {self.reg_def['offset']}  |  Reset = {self.reg_def['reset']}"
        )
        offset_lbl.setObjectName("subLabel")
        hdr.addWidget(offset_lbl)
        hdr.addStretch()

        reset_btn = QPushButton("\u21ba  Reset All")
        reset_btn.setObjectName("resetBtn")
        reset_btn.clicked.connect(self._reset_all)
        hdr.addWidget(reset_btn)

        copy_btn = QPushButton("\u2398  Copy Hex")
        copy_btn.setObjectName("copyBtn")
        copy_btn.clicked.connect(self._copy_hex)
        hdr.addWidget(copy_btn)

        root.addLayout(hdr)

        desc_lbl = QLabel(self.reg_def["name"])
        desc_lbl.setObjectName("subLabel")
        root.addWidget(desc_lbl)

        # ── 32-BIT REGISTER MAP (interactive, clickable) ───────────────────
        bm_group = QGroupBox("32-BIT REGISTER MAP  —  click any bit to toggle")
        bm_lay = QVBoxLayout(bm_group)
        bm_lay.setContentsMargins(8, 6, 8, 8)
        self.bit_map = BitMapWidget()
        self.bit_map.bit_toggled.connect(self._on_bit_toggled)
        bm_lay.addWidget(self.bit_map)

        # binary display row inside the map group
        bin_row = QHBoxLayout()
        bin_lbl = QLabel("Binary:")
        bin_lbl.setStyleSheet(f"color:{TEXT_MUTED}; font-size:11px;")
        bin_row.addWidget(bin_lbl)
        self.bin_label = QLabel("0000 0000  0000 0000  0000 0000  0000 0000")
        self.bin_label.setStyleSheet(
            f"font-family:'Consolas','Courier New',monospace; font-size:11px;"
            f"color:{ACCENT2}; letter-spacing:1px;"
        )
        bin_row.addWidget(self.bin_label)
        bin_row.addStretch()
        bm_lay.addLayout(bin_row)

        root.addWidget(bm_group)

        # ── Current value display + hex input/submit ───────────────────────
        val_group = QGroupBox("REGISTER VALUE")
        val_lay = QHBoxLayout(val_group)
        val_lay.setContentsMargins(12, 8, 12, 8)
        val_lay.setSpacing(14)

        val_lay.addWidget(QLabel("Current:"))
        self.hex_label = QLabel("0x00000000")
        self.hex_label.setObjectName("hexValue")
        val_lay.addWidget(self.hex_label)

        val_lay.addSpacing(30)

        # hex input
        input_lbl = QLabel("Load Hex:")
        input_lbl.setStyleSheet(f"color:{TEXT_MUTED}; font-size:12px;")
        val_lay.addWidget(input_lbl)

        self.hex_input = QLineEdit()
        self.hex_input.setObjectName("hexInput")
        self.hex_input.setPlaceholderText("e.g. 0x7F404D06  or  7F404D06")
        self.hex_input.setMaxLength(10)
        self.hex_input.setFixedWidth(200)
        self.hex_input.returnPressed.connect(self._submit_hex)
        val_lay.addWidget(self.hex_input)

        submit_btn = QPushButton("\u21d2  Apply")
        submit_btn.setObjectName("submitBtn")
        submit_btn.setFixedWidth(80)
        submit_btn.clicked.connect(self._submit_hex)
        val_lay.addWidget(submit_btn)

        self.hex_error_lbl = QLabel("")
        self.hex_error_lbl.setStyleSheet(f"color:{RED_ACCENT}; font-size:11px;")
        val_lay.addWidget(self.hex_error_lbl)

        val_lay.addStretch()
        root.addWidget(val_group)

        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.HLine)
        root.addWidget(sep)

        # ── Field rows in scroll area ──────────────────────────────────────
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        self.fields_layout = QVBoxLayout(container)
        self.fields_layout.setSpacing(2)
        self.fields_layout.setContentsMargins(0, 0, 0, 0)

        self.field_rows = []
        for i, field in enumerate(self.reg_def["fields"]):
            row = FieldRow(field)
            row.changed.connect(self._update_value)
            if i % 2 == 0:
                row.setStyleSheet(f"background: {CARD_BG}; border-radius:6px;")
            else:
                row.setStyleSheet(f"background: {PANEL_BG}; border-radius:6px;")
            self.fields_layout.addWidget(row)
            self.field_rows.append(row)

        self.fields_layout.addStretch()
        scroll.setWidget(container)
        root.addWidget(scroll)

        self._update_value()

    # ── Core compute / update ──────────────────────────────────────────────────

    def _compute_register(self):
        value = 0
        for row in self.field_rows:
            field = row.field
            hi, lo = field["bits"]
            width  = hi - lo + 1
            v = field["reset"] if field["type"] == "reserved" else row.get_value()
            value |= (v & ((1 << width) - 1)) << lo
        return value

    def _update_value(self):
        """Recompute hex from field widgets, refresh all displays."""
        if self._loading:
            return
        value = self._compute_register()
        self._refresh_displays(value)

    def _refresh_displays(self, value):
        """Push a 32-bit integer value into all display widgets (not field controls)."""
        self.hex_label.setText(f"0x{value:08X}")
        # grouped binary string: "1111 1111  1111 1111  1111 1111  1111 1111"
        bits = f"{value:032b}"
        groups = [bits[i:i+4] for i in range(0, 32, 4)]
        self.bin_label.setText(
            f"{groups[0]} {groups[1]}  {groups[2]} {groups[3]}  "
            f"{groups[4]} {groups[5]}  {groups[6]} {groups[7]}"
        )
        state = [(row.field, row.get_value()) for row in self.field_rows]
        self.bit_map.update_values(state)

    # ── Hex input → field decode ───────────────────────────────────────────────

    def _submit_hex(self):
        """Parse the hex input box and load all field widgets accordingly."""
        raw = self.hex_input.text().strip()
        if raw.lower().startswith("0x"):
            raw = raw[2:]
        raw = raw.replace(" ", "").replace("_", "")
        if not raw:
            self.hex_error_lbl.setText("Enter a hex value first.")
            return
        try:
            value = int(raw, 16)
        except ValueError:
            self.hex_error_lbl.setText("Invalid hex — use 0-9 / A-F only.")
            return
        if value > 0xFFFFFFFF:
            self.hex_error_lbl.setText("Value exceeds 32 bits (max FFFFFFFF).")
            return
        self.hex_error_lbl.setText("")
        self.hex_input.clear()
        self.load_from_value(value)

    def load_from_value(self, value):
        """
        Decode a 32-bit integer into all field widgets:
        - Sets combo/spin to the appropriate option matching the bit-slice.
        - Updates all displays atomically.
        """
        self._loading = True
        try:
            for row in self.field_rows:
                field = row.field
                if field["type"] == "reserved":
                    continue
                hi, lo = field["bits"]
                width  = hi - lo + 1
                mask   = (1 << width) - 1
                field_val = (value >> lo) & mask

                row._value = field_val

                if isinstance(row.sub_widget, QComboBox):
                    opt_vals = getattr(row, "_option_values", [])
                    if field_val in opt_vals:
                        idx = opt_vals.index(field_val)
                    else:
                        # pick closest option
                        idx = min(range(len(opt_vals)),
                                  key=lambda i: abs(opt_vals[i] - field_val)) if opt_vals else 0
                    row.sub_widget.blockSignals(True)
                    row.sub_widget.setCurrentIndex(idx)
                    row.sub_widget.blockSignals(False)
                    # update _value to what the combo actually represents
                    if opt_vals:
                        row._value = opt_vals[idx]

                elif isinstance(row.sub_widget, QSpinBox):
                    row.sub_widget.blockSignals(True)
                    row.sub_widget.setValue(field_val)
                    row.sub_widget.blockSignals(False)
        finally:
            self._loading = False

        # refresh displays with the exact value the caller supplied
        self._refresh_displays(value)
        # also sync the bit-map colours to the actual field values
        state = [(row.field, row.get_value()) for row in self.field_rows]
        self.bit_map.update_values(state)

    # ── Bit-map click handler ──────────────────────────────────────────────────

    def _on_bit_toggled(self, bit_idx, new_val):
        """
        A bit in the register map was clicked.  Determine which field owns
        that bit, enable the row, and update its widget to reflect the new
        bit value while leaving all other bits in that field unchanged.
        """
        # build current register value, flip the one bit
        current = self._compute_register()
        if new_val == 1:
            new_reg = current | (1 << bit_idx)
        else:
            new_reg = current & ~(1 << bit_idx)
        self.load_from_value(new_reg)

    # ── Actions ────────────────────────────────────────────────────────────────

    def _reset_all(self):
        for row in self.field_rows:
            row.reset()

    def _copy_hex(self):
        QApplication.clipboard().setText(self.hex_label.text())
        orig = self.hex_label.text()
        self.hex_label.setText("Copied!")
        QTimer.singleShot(1000, lambda: self.hex_label.setText(orig))


# ── Main window ───────────────────────────────────────────────────────────────

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MCT8329A Register Configurator")
        self.setMinimumSize(1080, 720)
        self.resize(1280, 820)
        self._reg_buttons = []
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        outer = QVBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # top bar
        top_bar = QWidget()
        top_bar.setStyleSheet(f"background:{PANEL_BG}; border-bottom:1px solid #D8DCE3;")
        top_bar.setFixedHeight(60)
        top_lay = QHBoxLayout(top_bar)
        top_lay.setContentsMargins(20, 0, 20, 0)

        logo = QLabel("\u2699  MCT8329A")
        logo.setStyleSheet(f"font-size:16px; font-weight:800; color:{ACCENT}; letter-spacing:1px;")
        top_lay.addWidget(logo)

        chip_lbl = QLabel("Motor Controller \u2014 Register Configuration Tool")
        chip_lbl.setStyleSheet(f"font-size:12px; color:{TEXT_MUTED}; margin-left:12px;")
        top_lay.addWidget(chip_lbl)
        top_lay.addStretch()

        outer.addWidget(top_bar)

        # landing area
        self.stack = QWidget()
        stack_lay = QVBoxLayout(self.stack)
        stack_lay.setContentsMargins(40, 30, 40, 30)
        stack_lay.setSpacing(18)

        welcome = QLabel("Select a Register to Configure")
        welcome.setStyleSheet(f"font-size:18px; font-weight:700; color:{TEXT_PRIMARY};")
        stack_lay.addWidget(welcome)

        hint = QLabel("Click a register button below to open its configuration panel in a new tab.")
        hint.setObjectName("subLabel")
        stack_lay.addWidget(hint)

        # search box
        self.search_box = QLineEdit()
        self.search_box.setObjectName("searchBox")
        self.search_box.setPlaceholderText("Filter registers by name or offset\u2026")
        self.search_box.textChanged.connect(self._filter_registers)
        stack_lay.addWidget(self.search_box)

        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.HLine)
        stack_lay.addWidget(sep)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        grid_container = QWidget()
        self.reg_grid = QGridLayout(grid_container)
        self.reg_grid.setSpacing(12)

        cols = 3
        for i, acr in enumerate(REGISTER_ORDER):
            reg_def = REGISTERS[acr]
            btn = QPushButton(f"{acr}\n{reg_def['offset']}")
            btn.setObjectName("registerBtn")
            btn.setFixedHeight(56)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda checked=False, a=acr: self._open_register(a))
            row, col = divmod(i, cols)
            self.reg_grid.addWidget(btn, row, col)
            self._reg_buttons.append((acr, btn))

        scroll.setWidget(grid_container)
        stack_lay.addWidget(scroll)

        # tab widget (starts with welcome)
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self._close_tab)

        welcome_tab = self.stack
        self.tabs.addTab(welcome_tab, "Home")
        self.tabs.tabBar().setTabButton(0, self.tabs.tabBar().RightSide, None)  # no close on home

        outer.addWidget(self.tabs)

    def _filter_registers(self, text):
        text = text.strip().lower()
        for acr, btn in self._reg_buttons:
            reg_def = REGISTERS[acr]
            haystack = f"{acr} {reg_def['offset']} {reg_def['name']}".lower()
            btn.setVisible(text in haystack)

    def _open_register(self, acronym):
        for i in range(self.tabs.count()):
            if self.tabs.tabText(i) == acronym:
                self.tabs.setCurrentIndex(i)
                return
        reg_def = REGISTERS[acronym]
        tab = RegisterTab(acronym, reg_def)
        idx = self.tabs.addTab(tab, acronym)
        self.tabs.setCurrentIndex(idx)

    def _close_tab(self, index):
        if index == 0:
            return  # never close Home
        self.tabs.removeTab(index)


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(DARK_BG))
    palette.setColor(QPalette.WindowText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Base, QColor(PANEL_BG))
    palette.setColor(QPalette.AlternateBase, QColor(CARD_BG))
    palette.setColor(QPalette.Text, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Button, QColor(CARD_BG))
    palette.setColor(QPalette.ButtonText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Highlight, QColor(ACCENT))
    palette.setColor(QPalette.HighlightedText, QColor("#0D1117"))
    app.setPalette(palette)
    app.setStyleSheet(STYLE_SHEET)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()