const randColor = () => {
  return (
    "#" +
    Math.floor(Math.random() * 16777215)
      .toString(16)
      .padStart(6, "0")
      .toUpperCase()
  );
};

// $(".hero").css("color", randColor())

// Access the context data safely
const mydata = JSON.parse(document.getElementById("mydata").textContent);

// Get the canvas element by id
const ctxcocnpOrder = document.getElementById("cocnporder").getContext("2d");

// Define your data
const datacocnpOrder = mydata[0].dataOrder;

// Create the chart
const cocnporder = new Chart(ctxcocnpOrder, {
  type: "bar",
  data: datacocnpOrder,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

// Get the canvas element by id
const ctxcocnpInventory = document
  .getElementById("cocnpinventory")
  .getContext("2d");

// Define your data
const datacocnpInventory = mydata[0].dataInventory;

// Create the chart
const cocnpinventory = new Chart(ctxcocnpInventory, {
  type: "bar",
  data: datacocnpInventory,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

// Get the canvas element by id
const ctxcnpOrder = document.getElementById("cnporder").getContext("2d");

// Define your data
const datacnpOrder = mydata[0].dataOrder;

// Create the chart
const cnporder = new Chart(ctxcnpOrder, {
  type: "bar",
  data: datacnpOrder,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

// Get the canvas element by id
const ctxcnpInventory = document
  .getElementById("cnpinventory")
  .getContext("2d");

// Define your data
const datacnpInventory = mydata[0].dataInventory;

// Create the chart
const cnpinventory = new Chart(ctxcnpInventory, {
  type: "bar",
  data: datacnpInventory,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

$(document).ready(function () {
  var flipster = $("#indentCarousel").flipster({});

  $(".btn").on("click", function () {
    const filter = $(this).data("filter");
    flipster.flipster("jump", 0); // Reset carousel to the first item

    // Filter Flipster items based on category
    if (filter === "all") {
      flipster.find("li").show();
    } else {
      flipster.find(`li:not(.${filter})`).hide();
      flipster.find(`li.${filter}`).show();
    }
  });
});

