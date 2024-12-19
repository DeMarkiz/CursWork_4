// Получаем данные из атрибута HTML
const chartDataElement = document.getElementById('chart-data');
const attemptSuccessCount = parseInt(chartDataElement.getAttribute('data-success'), 10);
const attemptFailureCount = parseInt(chartDataElement.getAttribute('data-failure'), 10);

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar', // тип графика
    data: {
        labels: ['Успешно', 'Неуспешно'],
        datasets: [{
            label: '# of Attempts',
            data: [attemptSuccessCount, attemptFailureCount],
            backgroundColor: [
                'rgba(255, 165, 0, 0.6)', // Оранжевый для успешных попыток с большей непрозрачностью
                'rgba(0, 0, 0, 0.6)'      // Черный для неудачных попыток с большей непрозрачностью
            ],
            borderColor: [
                'rgba(255, 165, 0, 1)',  // Оранжевый для успешных попыток
                'rgba(0, 0, 0, 1)'       // Черный для неудачных попыток
            ],
            borderWidth: 2, // Толщина границ
            borderRadius: 5 // Закругленные углы
        }]
    },
    options: {
        responsive: true, // Адаптивность графика
        plugins: {
            legend: {
                display: true,
                position: 'top',
                labels: {
                    color: '#ffffff', // Белые метки легенды
                    font: {
                        size: 14, // Размер шрифта
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#ffffff', // Белый цвет меток по оси Y
                    font: {
                        size: 14, // Размер шрифта оси Y
                    }
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.2)' // Легкая сетка
                }
            },
            x: {
                ticks: {
                    color: '#ffffff', // Белый цвет меток по оси X
                    font: {
                        size: 14, // Размер шрифта оси X
                    }
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.2)' // Легкая сетка
                }
            }
        }
    }
});
