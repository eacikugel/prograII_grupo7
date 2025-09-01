from Subject import WeatherData
from displays import CurrentConditionsDisplay, ForecastDisplay, StatisticsDisplay

def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    stats_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    print("Weather Station 1.0 (Versión PULL)")
    print("----------------------------------")

    print("\n[1] -> Se actualizan las mediciones en WeatherData")
    print("[2] -> WeatherData notifica a los observers: 'Hubo un cambio'")
    print("[3] -> Cada observer hace un PULL y pide los datos que necesita al WeatherData")
    weather_data.set_measurements(26.6, 65, 30.4)

    print("---")

    print("[Nueva actualización: los observers vuelven a hacer PULL de los datos]")
    weather_data.set_measurements(27.7, 70, 29.2)

    print("---")

    print("[Nueva actualización: los observers vuelven a hacer PULL de los datos]")
    weather_data.set_measurements(25.5, 90, 29.2)

    print("---")

    # Ejemplo de desregistro
    print("\n--- Forecast display se da de baja ---")
    weather_data.remove_observer(forecast_display)

    print("[Última actualización con solo CurrentConditions y Statistics]")
    weather_data.set_measurements(28.0, 88, 30.0)

if __name__ == "__main__":
    main()
