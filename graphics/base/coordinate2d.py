"""In diesem Modul wird eine 2-dimensionale Koordinate implementiert."""

# -----------------------------------------------------------------------------

from graphics.base.util import check_float
from typing_extensions import Self

# -----------------------------------------------------------------------------

class Coordinate2D:
    """Die Implementierung einer 2-dimensionalen Koordinate."""
    def __init__(self, x: float, y: float) -> None:
        """C'tor.

        Args:
            x: float: X-Koordinate.
            y: float: Y-Koordinate.
        """
        self._x = check_float(x, 'x')
        self._y = check_float(y, 'y')
        pass

    def get_x(self) -> float:
        """Getter fuer die X-Koordinate."""
        return self._x

    def get_y(self) -> float:
        """Getter fuer die Y-Koordinate."""
        return self._y

    @property
    def x(self) -> float:
        """Ein Getter als 'property'.
        
        c0: Coordinate2D = Coordinate2D(0, 0)
        print(c0.x)

        Returns:
            float: Gibt den internen Wert der Instanz zurueck.
        """
        return self._x

    @x.setter
    def x(self, value: float) -> Self:
        """Ein Setter fuer x.
        
        c0: Coordinate2D = Coordinate2D(0, 0)
        c0.x = 42.0
        
        Args:
            value: float: 
                Ein neuer Wert, der der Instanz fuer seine
                X-Koordinate zugewiesen wird.            

        Returns:
            Self: Eine Referenz auf diese Instanz.
        """
        self._x = float
        return Self

    def __eq__(self, other: 'Coordinate2D') -> bool:
        """Implementierung fuer einen Gleichheitsoperator (==-Operator).

        c0: Coordinate2D = Coordinate2D(0, 0)
        c1: Coordinate2D = Coordinate2D(0, 1)
        if c0 == c1:
            ...

        Args:
            other: 'Coordinate2D': Eine andere Koordinate.

        Returns:
            bool: Berechnet: (self.x == other.x) and (self.y == other.y)
        """
        if isinstance(other, self.__class__):
            return self.get_x() == other.get_x() and self.get_y() == other.get_y()
        else:
            return False

    def __ne__(self, other: 'Coordinate2D') -> bool:
        """Implementierung des Negierungsoperators (!=-Operator)

        Siehe __eq__.        

        Args:
            other: 'Coordinate2D': Eine andere Koordinate.

        Returns:
            bool: Berechnet: !(self == other)
        """
        return not self.__eq__(other)

    pass
# -----------------------------------------------------------------------------
